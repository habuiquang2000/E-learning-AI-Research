from django.urls import path
from django.views.generic import TemplateView

from .views import TeacherContactsView

urlpatterns = [
    path("contact/", TeacherContactsView.as_view(), name="contact"),
    # path("profile/", Profile.as_view(), name="profile"),
    # path("profile/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="user/about.html"), name="about"),
]
