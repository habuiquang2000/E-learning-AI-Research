from bs4 import BeautifulSoup
from django import template
from html import unescape

from django.db.models import Count, Value
from django.http import JsonResponse

from _scope.method import get
from _scope.subjects import extract_subject_children
from _utils.to_dict import to_dict
from _utils.query_debugger import query_debugger
from Document.models import Subject, Lesson
from gTTSApp.gTTS_module import text2Audio

# Create your views here.
register = template.Library()


@register.filter()
def plaintext(richtext):
    return BeautifulSoup(unescape(richtext), "html.parser").get_text(separator=" ")


@query_debugger
def get_tree_by_subject(req):
    subject_slug = get(req, "subject", "")
    chapter_slug = get(req, "chapter", "")

    subjects_query = Subject.objects
    subject = subjects_query\
        .filter(slug=subject_slug)\
        .annotate(
            childrenCount=Count("children"),
            isRoot=Value(True)
            # chapters=Chapter
        ).select_related("category")\
        .first()
    subject = to_dict(
        subject,
        extract_subject_children,
        "childrenCount",
        "isRoot",
        chapter_slug=chapter_slug,
    )

    context = {
        "data": subject
    }
    return JsonResponse(
        context,
        safe=True
    )


@query_debugger
def get_audio(req):
    lesson_slug = get(req, "lesson", "")
    audio_path = ''
    
    lessons_query = Lesson.objects
    lesson_queryset = lessons_query\
        .filter(slug=lesson_slug)\
        .first()

    if lesson_queryset is not None:
        audio_path = lesson_queryset.audio_file.name

        if audio_path.strip() == "":
            audio_path = text2Audio(
                lang="vi",
                text=plaintext(lesson_queryset.content).replace(",", "").replace(".", ""),
                # text=plaintext("<p>Xin chào</p>"),
            ).replace("%5C", "/")

            lesson_queryset.audio_file.name = audio_path
            lesson_queryset.save()

    context = {
        # "mp3": lesson
        "data": {
            "mp3": audio_path
        }
    }
    return JsonResponse(
        context,
        safe=True
    )


@query_debugger
def get_lesson(req):
    lesson_slug = get(req, "lesson", None)

    context = {
        "data": {}
    }

    if lesson_slug is not None and lesson_slug != "":
        lessons_query = Lesson.objects
        lesson_queryset = lessons_query\
            .filter(slug=lesson_slug)\
            .first()

        context["data"] = to_dict(lesson_queryset)

    return JsonResponse(
        context,
        safe=True
    )


# class FullTextSearchView(View):
#     def get(self, req):
#         query = req.GET.get("q", "")
#         qs = Lesson.objects

#         # FEATURE SEARCH
#         # qs = qs.filter(title__icontains=query)
#         # qs = qs.filter(title__unaccent__lower__trigram_similar=query)

#         # FULL-TEXT SEARCH
#         qs = qs.annotate(
#             search=SearchVector(
#                 "title",
#                 "caption",
#                 "content"
#             )
#         ).filter(
#             search=SearchQuery(query)
#         )

    # SEARCH HEADLINE()
    # used to highlight the results if query matches with the content
    # qs = qs.annotate(
    #     headline=SearchHeadline(
    #         "content",
    #         SearchQuery(query),
    #         start_sel="<span style="font-weight: bold; background: yellow">",
    #         stop_sel="</span>",
    #     )
    # )

    # context = {
    #     "q": query,
    #     "queryset": qs
    # }
    # return render(req, "user/full-text-search.html", context)
