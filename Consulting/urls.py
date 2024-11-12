from django.urls import path
from django.views.generic import TemplateView
# from .views import DocumentListView, DocumentDetailView, FullTextSearchView

urlpatterns = [
    path("", TemplateView.as_view(template_name="user/consulting/chat.html"), name="consulting_chat"),
]
