from os import path, makedirs, remove
from shutil import rmtree
from sys import version_info
from uuid import uuid4 as uuid
# from datetime import datetime

from gtts import gTTS
# from .models import Speech

from django import template
from django.conf import settings
# try:
# Django 2
# from django.contrib.staticfiles.templatetags.staticfiles import static
# except ModuleNotFoundError:
# Django 3
from django.templatetags.static import static

cur_dir = path.join(path.dirname(path.abspath(__file__)), "..")
dir_name = "gTTS"
temp_path = path.join(
    cur_dir,
    path.join(
        getattr(settings, "STATIC_URL", " ")[1:],
        dir_name
    )
)

register = template.Library()


def remove_cache():
    """ 
    remove cache folder and Speech modal records 
    """
    if path.isdir(temp_path):
        rmtree(temp_path)
    # Speech.objects.all().delete()


@register.simple_tag
def text2Audio(lang="en-us", text="Flask says Hi!"):
    # info = {
    #     "lang": lang,
    #     "text": text
    # }

    # for key, val in info.items():
    #     if not isinstance(val, str):  # check if receiving a string
    #         raise (TypeError("gTTS.say(%s) takes string" % key))

    # try:
    #     speech_query = Speech.objects

    #     audio_file = speech_query.get(text=text, language=lang)
    #     file_dir = path.join(temp_path, audio_file.file_name)

    #     if not path.isfile(file_dir):
    #         records_to_delete = speech_query.filter(
    #             text=text, language=lang
    #         ).all()

    #         for records in records_to_delete:
    #             records.delete()

    #         audio_file = None
    # except Exception:
    #     audio_file = None

    if not path.isdir(temp_path):  # creating temporary directory
        makedirs(temp_path) if version_info.major == 2 else makedirs(
            # makedirs in py2 missing exist_ok
            temp_path, exist_ok=True
        )

    # if audio_file is None:
    gTTS_file = gTTS(
        text=text,
        tld="com.vn",
        lang=lang
    )

    while True:  # making sure audio file name is truly unique
        fname = str(uuid()) + ".mp3"
        abp_fname = path.join(temp_path, fname)
        if not path.isfile(abp_fname):
            break

        # Speech(
        #     text=text,
        #     language=lang,
        #     file_name=fname
        # ).save()

    gTTS_file.save(abp_fname)
    # else:
    #     fname = audio_file.file_name

    return static("/".join([dir_name, fname]))

# class DocCreate(View):
#     def post(self, req):
#         student_id = post(req, "student_id")
#         student_name = post(req, "student_name")
#         title = post(req, "title")
#         shortDescription = post(req, "shortDescription")
#         description = post(req, "description")
#         cate = post(req, "cate")
#         message = post(req, "message")
#         doc_file = req.FILES["doc_file"]
#         image = req.FILES["image"]
#         file = req.FILES["file"]

#         doc = Document(
#             student_id=get_object_or_404(User, id=student_id),
#             student_name=student_name,
#             title=title,
#             shortDescription=shortDescription,
#             description=description,
#             cate=get_object_or_404(SubCategory, id=cate),
#             message=message,
#             doc_file=doc_file,
#             image=image,
#             file=file
#         )
#         doc.save()
#         messages.success(req, "nộp bài thành công")
#         return redirect("doc_create")
