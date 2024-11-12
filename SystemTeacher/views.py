from django.shortcuts import render, redirect
from django.views import View

from _scope.method import get, post
# from SystemUser.models import Classmate, Department
# import csv
# import datetime
# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from import_export import resources
# from django.contrib import messages
# from tablib import Dataset

from Consulting.models import Answer, Question
from Document.models import Lesson
# Create your views here.


class QuestionNoAnswerList(View):
    def get(self, req):
        question_query = Question.objects
        question = question_query.filter(answer=None)

        context = {
            "question": question,
            "count": question.count(),

            "has_permission": True,
            "site_url": "/",
        }
        return render(req, "admin/custom/question-no-answer-list.html", context)


class QuestionNoAnswerDetail(View):
    def get(self, req, id):
        question_query = Question.objects
        question = question_query.filter(id=id).first()

        context = {
            "question": question,
        }
        return render(req, "admin/custom/question-no-answer-detail.html", context)

    def post(self, req, id):
        answer = post(req, "answer", "")
        keyword = post(req, "keyword", "")

        question = Question.objects.filter(id=id).first()

        answer = Answer(
            content=answer,
            keyword=keyword,
        )

        if question:
            answer.save()
            question.answer = answer
            question.save()
            return redirect("question_no_answer_list")

        context = {
            "question": question,
        }
        return render(req, "admin/custom/question-no-answer-detail.html", context)


class AnswerTrainList(View):
    def get(self, req):

        return render(req, "admin/custom/answer-train-list.html")


class DocumentFromOffice(View):
    def get(self, req):
        context = {
        }
        return render(req, "admin/custom/document-from-office.html", context)


class AnswerTrainDetail(View):
    def get(self, req, slug):
        return render(req, "admin/custom/add_student_list.html")

    def post(self, req):
        if post(req, "type") == "1":
            count = post(req, "count")

            pushData = []
            for key, value in req.POST.items():
                if key != "csrfmiddlewaretoken" and key != "type" and key != "count":
                    pushData.append(value)

            for i in range(int(count)):
                obj = pushData[0:6]

                if User.objects.filter(id=obj[0]).exists() or User.objects.filter(email=obj[4]).exists():
                    user = User.objects.get(id=obj[0])
                    user.set_password(obj[5])
                    user.save()
                    messages.warning(
                        req, "đã đổi mật khẩu cho sinh viên {}".format(obj[0]))
                else:
                    class_id = get_object_or_404(Classmate, class_id=obj[3])
                    user = User(
                        id=obj[0],
                        first_name=obj[1],
                        last_name=obj[2],
                        class_id=class_id,
                        email=obj[4],
                        password=obj[5],
                        username=obj[0],
                    )
                    user.save()
                    messages.success(
                        req, "thêm sinh viên {} thành công".format(obj[0]))
                del pushData[0:6]

            context = {
                "mess": 1,
                "page": 1,
            }
        if post(req, "type") == "0":
            if req.FILES:
                file_datas = req.FILES["file"]
                file_name = file_datas.name
                if file_name.endswith("xls"):
                    import_data = Dataset().load(file_datas.read(), format="xls")

                elif file_name.endswith("xlsx"):
                    import_data = Dataset().load(file_datas.read(), format="xlsx")

                elif file_name.endswith("csv"):
                    import_data = Dataset().load(file_datas.read(), format="xls")

            person = []
            # print(type(User.objects.all()))
            for data in import_data:
                person.append({
                    "id": data[0],
                    "first_name": data[1],
                    "last_name": data[2],
                    "class_id": data[3],
                    "email": data[4],
                    "password": data[5],
                    "username": data[0],
                })

            context = {
                "page": 1,
                "person": person,
                "count": "0{}".format(len(person))[:2],
            }
        return render(req, "add_student_list.html", context)


class StudentDetails(View):
    def get(self, req, slug):
        classmate = Classmate.objects.filter(class_id=slug)
        doc = Document.objects.all()
        context = {
            "class": classmate,
            "count": "0{}".format(doc.count())[:2],
            "doc": doc,
        }
        return render(req, "class_details.html", context)

    def post(self, req, slug):
        type = post(req, "action")
        if type == "0":
            doc = Document.objects.all()
        else:
            doc = Document.objects.filter(type_of_exercise=type)
        context = {
            "class": slug,
            "count": "0{}".format(doc.count())[:2],
            "doc": doc,
            "selected": type,
        }
        return render(req, "class_details.html", context)


class ExportCsv(View):
    def get(self, req):
        class_id = get(req, "class_id")
        choose = get(req, "choose")

        res = HttpResponse(content_type="text/csv")
        res["Content-Disposition"] = "attachment; filename={}".format(
            str(datetime.datetime.now()) + ".csv")
        res.write(u"\ufeff".encode("utf8"))
        writer = csv.writer(res)
        writer.writerow(["Họ và tên", "Mã sinh viên", "Lớp",
                        "Loại đồ án", "Ngày nộp bài"])

        if choose == "0":
            doc = Document.objects.all()
        else:
            classmate = Classmate.objects.get(class_id=class_id)
            doc = Document.objects.filter(
                type_of_exercise=choose, student_class=class_id)
        for user in doc.values_list("student_name", "student_id", "student_class", "type_of_exercise", "created"):
            writer.writerow(user)

        return res
