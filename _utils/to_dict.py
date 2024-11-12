# import json
from itertools import chain
from django.db.models.fields.files import ImageFieldFile, FieldFile


def to_dict(instance, call_back_children=None, *args, **kwargs):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        val = f.value_from_object(instance)
        if isinstance(val, ImageFieldFile):
            image = val.instance.image
            data[f.name] = image.url if image else ""
        if isinstance(val, FieldFile):
            image = val.instance.image
            data[f.name] = image.url if image else ""
        else:
            data[f.name] = val

    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]

    for arg in args:
        if hasattr(instance, arg):
            data[arg] = getattr(instance, arg)

    if hasattr(instance, "children"):
        if instance.children and call_back_children is not None:
            data["children"] = call_back_children(instance, kwargs)

    return data


# from django.db.models import Count, Prefetch
# from django.contrib.auth.models import User
# from django.contrib.sessions.models import Session
# from django.core import serializers
# from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse


# prices_and_programs = Subject.objects.select_related("children")
# subjects = subjects_query.prefetch_related(
# Prefetch("children", queryset=prices_and_programs)
# Prefetch("children", Subject.objects, to_attr="children")
# Chapter
# )
# serialized_data = serializers.serialize("json", subjects.values())
# serialized_data = json.loads(serialized_data)
# subjects_list = list(subjects.values())


# class CustomEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, ImageFieldFile):
#             return None
#             # Do whatever appropriate for your case, like returning None
#         return super(CustomEncoder, self).default(obj)

# \views.py
# "data": serialized_data
# return JsonResponse(
#     content,
#     # encoder=CustomEncoder,
#     safe=True
# )
    # posts = Post.objects.filter(
    #     published_at__isnull=False).order_by("-published_at")
    # post_list = serializers.serialize("json", posts)
    # return HttpResponse(post_list, content_type="text/json-comment-filtered")

    # qs_json = serializers.serialize("json", qs)
    # return HttpResponse(qs_json, content_type="application/json")
    # subjects = Subject.objects.values()
    # subjects = Subject.objects.filter(
    #     title__icontains=""
    # ).values()

    # return HttpResponse(
    #     # content
    #     # json.dumps(content, indent=4),
    #     serializers.serialize(
    #         "json",
    #         content
    #     ),
    #     content_type="application/json"
    # )
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in the publisher
    #     context["category"] = self.category
    #     print(   context["category"])
    #     return context

# https://example.com/?fruits=apple&meat=beef
# print(request.GET["fruits"]) # apple
# print(request.GET.get("meat")) # beef
# print(request.GET.get("fish")) # None
# print(request.GET.get("fish", "Doesn"t exist")) # Doesn"t exist
# print(request.GET.getlist("fruits")) # ["apple"]
# print(request.GET.getlist("fish")) # []
# print(request.GET.getlist("fish", "Doesn"t exist")) # Doesn"t exist
# print(request.GET._getlist("meat")) # ["beef"]
# print(request.GET._getlist("fish")) # []
# print(request.GET._getlist("fish", "Doesn"t exist")) # Doesn"t exist
# print(list(request.GET.keys())) # ["fruits", "meat"]
# print(list(request.GET.values())) # ["apple", "beef"]
# print(list(request.GET.items())) # [("fruits", "apple"), ("meat", "beef")]
# print(list(request.GET.lists())) # [("fruits", ["apple"]), ("meat", ["beef"])]
# print(request.GET.dict()) # {"fruits": "apple", "meat": "beef"}
# print(dict(request.GET)) # {"fruits": ["apple"], "meat": ["beef"]}
# print(request.META["QUERY_STRING"]) # fruits=apple&meat=beef
# print(request.META.get("QUERY_STRING")) # fruits=apple&meat=beef
# {# "index.html" #}

# {{ request.GET.fruits }} {# apple #}
# {{ request.GET.meat }} {# beef #}
# {{ request.GET.dict }} {# {"fruits": "apple", "meat": "beef"} #}
# {{ request.META.QUERY_STRING }} {# fruits=apple&meat=beef #}

# from django.urls import resolve
# resolveMatcher = resolve(request.path)
# userName = resolveMatcher.kwargs.get("userName", None)


# {% url "order_list" %}?office=foobar&{{ request.GET.urlencode }}


# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     "django.core.context_processors.request",
# )

# <a href="{% url "myview" %}?office={{ some_var | urlencode }}">

    # if not request.session.session_key:
    #     request.session.create()

    # print(request.session.session_key)

    # from django.conf import settings
    # session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]
    # request.COOKIES["sessionid"]

    # session_key  = req.session.session_key

    # session = Session.objects.get(session_key=session_key)
    # session_data = session.get_decoded()
    # uid = session_data.get("_auth_user_id")
    # user = User.objects.get(id=uid)

    # serialized_data = serializers.serialize("json", subjects.values())
    # serialized_data = json.loads(serialized_data)
    # "data": subjects
    # "data": subjects_list
    # "data": serialized_data


# https://code.djangoproject.com/ticket/21238
# I don"t understand. django.core.files.base.File has only one parent, which is django.core.files.utils.FileProxyMixin which does not have __init__ method.
# # I try to do this in django/core/files/base.py:
#     def __init__(self, file, name=None):
# +       super(File, self).__init__()
#         self.file = file
#         if name is None:
#             name = getattr(file, "name", None)
#         self.name = name
#         if hasattr(file, "mode"):
#             self.mode = file.mode
# +       # or even this, but it does not work
# +       # super(File, self).__init__()


# https://github.com/nephila/django-meta/issues/124
# class News(ModelMeta, models.Model):
#     title = models.CharField(max_length=200)
#     content= RichTextUploadingField()
#     date = models.DateTimeField("published_date")
#     image = models.ImageField(upload_to="images", blank=False)
#     category = models.ForeignKey(
#         Category, default=1, verbose_name="Categories",
#         on_delete=models.SET_DEFAULT)
#     post_slug = AutoSlugField(populate_from="title")

#     _metadata = {
#         "title": "title",
#         "image": "image",
#     }

#     def get_meta_image(self):
#         if self.image:
#             return self.image.url

#     def __str__(self):
#         return self.title

    # _metadata = {
    #     "title": "title",
    #     "image": "get_meta_image",
    # }


# <head  prefix="og: http://ogp.me/ns#">
#   <title>bump of chicken</title>
# <meta name="description" content="News">
# </head>


# <html>
# {% load meta %}
# <head {% meta_namespaces %}>
#   <title>{{post.title}}</title>
#   {% include "meta/meta.html" %}
# </head>


# def single_slug(request, single_slug):
#     news = [p.post_slug for p in News.objects.all()]
#     if single_slug in news:
#         this_post = News.objects.get(post_slug=single_slug)
#         meta = this_post.as_meta()

#         return render(request=request,
#                       template_name="main/posts.html",
#                       context={"post": this_post, "meta": meta
#                                })

# class News(ModelMeta, models.Model):
#     title = models.CharField(max_length=200)
#     content = RichTextUploadingField()
#     datetime = models.DateTimeField("published date")
#     image = models.ImageField(upload_to="images", blank=False)
#     post_slug = AutoSlugField(populate_from="title")
#     category = "Notícia"

#     _metadata = {
#         "title": "title",
#         "description": "category",
#         "image": "get_meta_image",
#         "url": "post_slug",
#     }

#     def __str__(self):
#         return self.título

#     def get_meta_image(self):
#         if self.image:
#             return self.image.url


# https://itecnote.com/tecnote/imagefieldfile-object-has-no-attribute-content_type-only-after-picture-has-already-been-uploaded-then-isnt-either-changed-or-removed/
# class UserProfileForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(UserProfileForm, self).__init__(*args, **kwargs)
#         try:
#             self.fields["email"].initial = self.instance.user.email
#         except User.DoesNotExist:
#             pass

#     email = forms.EmailField(label="Primary email", help_text="")

#     class Meta:
#         model = UserAccountProfile
#             exclude = ("user", "broadcaster", "type")
#             widgets = {
#             ...
#         }


#     def save(self, *args, **kwargs):
#         u = self.instance.user
#         u.email = self.cleaned_data["email"]
#         u.save()
#         profile = super(UserProfileForm, self).save(*args,**kwargs)
#         return profile

#     def clean_avatar(self):
#         avatar = self.cleaned_data["avatar"]

#         if avatar:
#             w, h = get_image_dimensions(avatar)
#             max_width = max_height = 500
#             if w >= max_width or h >= max_height:
#                 raise forms.ValidationError(u"Please use an image that is %s x %s pixels or less." % (max_width, max_height))

#             main, sub = avatar.content_type.split("/")
#             if not (main == "image" and sub in ["jpeg", "pjpeg", "gif", "png"]):
#                 raise forms.ValidationError(u"Please use a JPEG, GIF or PNG image.")

#             if len(avatar) > (50 * 1024):
#                 raise forms.ValidationError(u"Avatar file size may not exceed 50k.")

#         else:
#             pass

#         return avatar


# from django.core.files.uploadedfile import UploadedFile
# from django.db.models.fields.files import ImageFieldFile

# def clean_avatar(self):
#     avatar = self.cleaned_data["avatar"]

#     if avatar and isinstance(avatar, UploadedFile):
#         w, h = get_image_dimensions(avatar)
#         max_width = max_height = 500
#         if w >= max_width or h >= max_height:
#             raise forms.ValidationError(u"Please use an image that is %s x %s pixels or less." % (max_width, max_height))

#         main, sub = avatar.content_type.split("/")
#         if not (main == "image" and sub in ["jpeg", "pjpeg", "gif", "png"]):
#             raise forms.ValidationError(u"Please use a JPEG, GIF or PNG image.")

#         if len(avatar) > (50 * 1024):
#             raise forms.ValidationError(u"Avatar file size may not exceed 50k.")

#     elif avatar and isinstance(avatar, ImageFieldFile):
#         # something
#         pass

#     else:
#         pass

#     return avatar


# ./manage.py dbshell

# DROP TABLE django_admin_log;

# class UserProfileForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(UserProfileForm, self).__init__(*args, **kwargs)
#         try:
#             self.fields["email"].initial = self.instance.user.email
#         except User.DoesNotExist:
#             pass

#     email = forms.EmailField(label="Primary email", help_text="")

#     class Meta:
#         model = UserAccountProfile
#             exclude = ("user", "broadcaster", "type")
#             widgets = {
#             ...
#         }


#     def save(self, *args, **kwargs):
#         u = self.instance.user
#         u.email = self.cleaned_data["email"]
#         u.save()
#         profile = super(UserProfileForm, self).save(*args,**kwargs)
#         return profile

#     def clean_avatar(self):
#         avatar = self.cleaned_data["avatar"]            

#         if avatar:
#             w, h = get_image_dimensions(avatar)
#             max_width = max_height = 500
#             if w >= max_width or h >= max_height:
#                 raise forms.ValidationError(u"Please use an image that is %s x %s pixels or less." % (max_width, max_height))

#             main, sub = avatar.content_type.split("/")
#             if not (main == "image" and sub in ["jpeg", "pjpeg", "gif", "png"]):
#                 raise forms.ValidationError(u"Please use a JPEG, GIF or PNG image.")

#             if len(avatar) > (50 * 1024):
#                 raise forms.ValidationError(u"Avatar file size may not exceed 50k.")

#         else:
#             pass

#         return avatar

# from django.core.files.uploadedfile import UploadedFile
# from django.db.models.fields.files import ImageFieldFile

# def clean_avatar(self):
#     avatar = self.cleaned_data["avatar"]            

#     if avatar and isinstance(avatar, UploadedFile):
#         w, h = get_image_dimensions(avatar)
#         max_width = max_height = 500
#         if w >= max_width or h >= max_height:
#             raise forms.ValidationError(u"Please use an image that is %s x %s pixels or less." % (max_width, max_height))

#         main, sub = avatar.content_type.split("/")
#         if not (main == "image" and sub in ["jpeg", "pjpeg", "gif", "png"]):
#             raise forms.ValidationError(u"Please use a JPEG, GIF or PNG image.")

#         if len(avatar) > (50 * 1024):
#             raise forms.ValidationError(u"Avatar file size may not exceed 50k.")

#     elif avatar and isinstance(avatar, ImageFieldFile):
#         # something
#         pass

#     else:
#         pass

#     return avatar