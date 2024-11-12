from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from _scope.method import get
from .models import Subject, Lesson

# from .forms import DocumentsForm
# from django.views.generic import TemplateView, ListView
# from django.contrib import messages


# Create your views here.

class DocumentListView(View):
    def get(self, req):
        search = get(req, "q", "")
        category_slug = get(req, "c", "")

        subject_query = Subject.objects

        if category_slug:
            subject_query = subject_query.filter(
                category__slug__icontains=category_slug
            )
        elif search != "":
            search_vector = SearchVector(
                "title",
                "slug",
                "children__title",
                "children__slug",
                "children__caption",
                "children__children__caption",
                "children__children__content",
            )
            search_query = SearchQuery(search)
            search_headline = SearchHeadline(
                "children__children__content",
                search_query,
                start_sel="""<span style="font-weight: bold; background: yellow;">""",
                stop_sel="""</span>""",
            )

            subject_query = subject_query\
                .annotate(
                    search=search_vector,
                    rank=SearchRank(search_vector, search_query)
                )\
                .annotate(headline=search_headline)\
                .filter(search=search_query)\
                .order_by("-rank")\
                .distinct()

        subjects = subject_query.annotate(
            chapter__count=Count("children")
        )

        context = {
            "subjects": subjects,
            "subjects_count": len(subjects),
            "q": search or "",
            "category_slug": category_slug or "",
            
            "page_range": 1,
            "limit": 10,
            "page": 1,
        }
        return render(req, "user/document/category.html", context)


class DocumentDetailView(View):
    def get(self, req):
        subject_slug = get(req, "subject", "")
        chapter_slug = get(req, "chapter", "")
        lesson_slug = get(req, "lesson", "")

        context = {
            "subject_slug": lesson_slug,
        }
        return render(req, "user/document/detail.html", context)


class FullTextSearchView(View):
    def get(self, req):
        query = req.GET.get("q", "")
        qs = Lesson.objects

        # FEATURE SEARCH
        # qs = qs.filter(title__icontains=query)
        # qs = qs.filter(title__unaccent__lower__trigram_similar=query)

        # FULL-TEXT SEARCH
        qs = qs.annotate(
            search=SearchVector(
                "title",
                "caption",
                "content"
            )
        ).filter(
            search=SearchQuery(query)
        )

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

        context = {
            "q": query,
            "queryset": qs
        }
        return render(req, "user/full-text-search.html", context)
