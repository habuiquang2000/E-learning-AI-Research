from django.db.models import Count, Case, When, Value, CharField

from _utils.to_dict import to_dict
from Document.models import Subject


def subject_list(req):
    subjects = Subject.objects.annotate(
        chapter__count=Count("children")
    )
    return {
        "subjects_template": subjects
    }


def extract_chapter_children(chapter, kwargs):
    return [
        *list(chapter.children.order_by("order").values())
    ]


def extract_subject_children(subject, kwargs):
    return [
        to_dict(
            chapter,
            extract_chapter_children,
            "childrenCount",
            "isExpand",
        )
        for chapter in subject.children.annotate(
            childrenCount=Count("children"),
            isExpand=Case(
                When(
                    slug=kwargs["chapter_slug"],
                    then=Value(True)
                ),
                default=Value(False),
                output_field=CharField())

        ).order_by("order")
    ]
