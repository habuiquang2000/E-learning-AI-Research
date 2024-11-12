import json
from django.http import JsonResponse

from _utils.query_debugger import query_debugger
from Consulting.models import Answer, Question


@query_debugger
def post_answer_train(req):
    context = {"data": "false"}

    if req.method == "POST" and req.body is not None:
        body_unicode = req.body.decode("utf-8")
        body = json.loads(body_unicode)
        data = body["data"]

        answers = [Answer(
            content=answer["content"],
            keyword=answer["keyword"],
        ) for answer in data]

        Answer.objects.bulk_create(answers)

        questions = [Question(
            question=data[i]["question"],
            answer=answers[i],
        ) for i in range(len(data))]

        Question.objects.bulk_create(questions)

        context["data"] = "true"

    return JsonResponse(
        context,
        safe=True
    )
