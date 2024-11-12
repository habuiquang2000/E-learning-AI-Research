import json
from django.db.models import Count
from django.http import JsonResponse
import docx2txt

from _scope.method import get
from _utils.to_dict import to_dict
from _utils.query_debugger import query_debugger
from Document.models import Category, Subject, Chapter, Lesson


# DOCUMENT CONTENT
@query_debugger
def get_categories(req):
    category_query = Category.objects

    category_dataset = category_query.annotate(
        childrenCount=Count("children"),
    )

    categories = [to_dict(
        category,
        None,
        "childrenCount",
    )for category in category_dataset]

    context = {
        "data": categories
    }
    return JsonResponse(
        context,
        safe=True
    )


@query_debugger
def get_chapters(req):
    subject_slug = get(req, "subject", "")
    chapter_query = Chapter.objects

    chapter_dataset = chapter_query.annotate(
        childrenCount=Count("children"),
    ).filter(subject__slug=subject_slug)

    chapters = [to_dict(
        chapter,
        None,
        "childrenCount",
    )for chapter in chapter_dataset]

    context = {
        "data": chapters
    }
    return JsonResponse(
        context,
        safe=True
    )


@query_debugger
def get_subjects(req):
    category_slug = get(req, "category", "")

    subject_query = Subject.objects

    subject_dataset = subject_query.annotate(
        childrenCount=Count("children"),
    ).filter(category__slug=category_slug)

    subjects = [to_dict(
        chapter,
        None,
        "childrenCount",
    )for chapter in subject_dataset]

    context = {
        "data": subjects
    }
    return JsonResponse(
        context,
        safe=True
    )


@query_debugger
def post_document_from_word(req):
    context = {"data": ""}

    if req.method == "POST" and req.FILES is not None:
        file = req.FILES.get('file')

        if file is not None:
            text = docx2txt.process(
                docx=file,
                # img_dir="D:\\"
            )

            content = []
            for line in text.splitlines():
                if line != '':
                    content.append(line.strip())

            context["data"] = "".join(map(str, content))

    return JsonResponse(
        context,
        safe=True
    )


@query_debugger
def post_document_from_content(req):
    context = {"data": "false"}

    if req.method == "POST" and req.body is not None:
        body_unicode = req.body.decode("utf-8")
        body = json.loads(body_unicode)
        data = body["data"]

        chapter = Chapter.objects.filter(slug=data["chapter"]).first()

        lesson = Lesson(
            title=data["title"],
            order=data["order"],
            caption=data["caption"],
            content=data["content"],
            chapter=chapter,
        )

        lesson.save()
        context["data"] = "true"

    return JsonResponse(
        context,
        safe=True
    )
