from django.urls import path
from django.contrib import admin
from .views import QuestionNoAnswerList, QuestionNoAnswerDetail, AnswerTrainList, AnswerTrainDetail, ExportCsv, DocumentFromOffice

urlpatterns = [
    path("question/no/answer/<id>/", QuestionNoAnswerDetail.as_view(), name="question_no_answer_detail"),
    path("question/no/answer/", QuestionNoAnswerList.as_view(), name="question_no_answer_list"),
    path("leson/content/<slug>", QuestionNoAnswerList.as_view(), name="lesson_content_detail"),
    path("leson/content/", DocumentFromOffice.as_view(), name="lesson_content_list"),
    
    path("answer/train/<slug>/", AnswerTrainDetail.as_view(), name="answer_list"),
    path("answer/train/", AnswerTrainList.as_view(), name="answer_list"),
    
    # path("class/", ClassDetails.as_view(), name="class_details"),
    # path("student/", StudentList.as_view(), name="student_list"),
    # path("student/add", StudentListAdd.as_view(), name="add_student"),
    # path("student/<slug>", StudentDetails.as_view(), name="student_details"),
    path("csv/", ExportCsv.as_view(), name="csv"),
    # path("class/<str:slug>", admin.site.urls),
    # path("student", admin.site.urls),
    # path("student", admin.site.urls),
    
    path("", admin.site.urls, name="teacher_manager"),
]
