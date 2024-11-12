from django.urls import path
from django.views.generic import TemplateView
# from .views import HomeDetailView

urlpatterns = [
    path("", TemplateView.as_view(template_name="user/document/home.html"), name="home"),
    # path("", HomeDetailView.as_view(), name="home"),
]
