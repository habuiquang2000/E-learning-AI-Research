from django.urls import path
from .views import DocumentListView, DocumentDetailView, FullTextSearchView

urlpatterns = [
    # path("<category_id>", DocList.as_view(), name="category"),
    path("full-text-search/", FullTextSearchView.as_view(), name="full_text_search"),
    path("detail/", DocumentDetailView.as_view(), name="document_detail"),
    path("", DocumentListView.as_view(), name="document_list"),
]
