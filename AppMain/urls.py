"""AppMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("api/", include("RestApi.urls"), name="app-api"),
    path("about/", include("About.urls"), name="about"),
    path("chat/", include("Consulting.urls"), name="consulting"),
    path("document/", include("Document.urls"), name="document"),

    path("gtts/", include("gTTSApp.urls")),

    path("teacher/", include("SystemTeacher.urls"), name="teacher"),
    path("user/", include("SystemUser.urls"), name="user"),
    path("", include("Home.urls"), name="home"),

    # re_path(r"^$", render_react),
    # re_path(r"^(?:.*)/?$", render_react),

    # Paymet
    # path("ckeditor/", include("ckeditor_uploader.urls")),
    # path("cart/", include("cart.urls")),
    re_path(
        r"^media/(?P<path>.*)$", serve,
        {"document_root": settings.MEDIA_ROOT}),
    re_path(
        r"^static/(?P<path>.*)$", serve,
        {"document_root": settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "catching_error.views.handler404"
handler500 = "catching_error.views.handler500"
