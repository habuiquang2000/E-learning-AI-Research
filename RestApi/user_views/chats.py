from django.contrib.postgres.search import SearchVector, SearchQuery
from django.http import JsonResponse

from _scope.method import get
from _utils.string2bool import str2bool
from _utils.query_debugger import query_debugger
from Consulting.models import Question


@query_debugger
def get_chat(req):
    question_param = get(req, "question", "")
    question_param = question_param.strip()

    isInit = str2bool(get(req, "isInit", ""))

    context = {"data": []}
    question_query = Question.objects

    if not isInit:
        search_vector = SearchVector(
            "answer__keyword",
            "question",
            "answer__content",
        )
        search_query = SearchQuery(question_param)

        question_query = question_query\
            .annotate(
                search=search_vector,
            )\
            .filter(search=search_query)\

        question_query

        if len(question_query) == 0 and question_param != "":
            Question(question=question_param).save()
            context["data"] = [
                {
                    "answer": "Câu hỏi cuả bạn chúng tôi sẽ trả lời trong thời gian sớm nhất!"
                },
            ]
        elif len(question_query) != 0 and question_param != "":
            question = question_query.first()
            if question.answer is not None:
                answer = question.answer.content
                context["data"] = [
                    {
                        "answer": answer
                    },
                ]
            else:
                context["data"] = [
                    {
                        "answer": "Câu hỏi cuả bạn chúng tôi sẽ trả lời trong thời gian sớm nhất!"
                    },
                ]

        elif question_param == "":
            context["data"] = [
                {
                    "answer": "Bạn cần nhập câu hỏi"
                },
            ]
        # if req.user.is_authenticated:
        #     user = req.user
        #     print(user)

        # subjects = subjects_query.annotate(
        #     chapter__count=Count("chapter"),
        #     # chapters=""
        # ).select_related("category")

        # subjects_list = list(subjects.values())
        # content = {
        #     "data": [
        #         {
        #             "question": "Hello Philip! :)",
        #             "answer": "Hi Sandy! How are you?"
        #         },
        #         {
        #             "question": "I\"m fine, thank you!",
        #             "answer": "123"
        #         },
        #     ]
        # }

            # headline=SearchHeadline(
            #     "slug",
            #     SearchQuery(search),
            #     start_sel="<span style="font-weight: bold; background: yellow">",
            #     stop_sel="</span>",)
            #     search=SearchVector(
            #     )

            # .filter(
            #     search=SearchQuery(search)
            # )
            # .order_by("id", "title")\
            #     "id",
            # "title",
            # "slug",
            # "children__title",
            # "children__slug",
            # "children__caption",
            # "children__children__caption",
            # "children__children__content",
            # )
            # .filter(
            #     # title__icontains=search,
            #     title__search=search,
            #     # title__unaccent__icontains=search,
            #     # title__unaccent__lower__trigram_similar=search
            # )
            # Quote.objects.annotate(
            # search=SearchVector("name", "quote")).filter(
            #     search=query
            # )
            # document = Document.objects.filter(title__search=q)
            # .annotate(headline=search_headline).filter(rank__gt=0.0001).order_by("-rank")

    return JsonResponse(
        context,
        safe=True
    )
