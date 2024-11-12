from django.urls import path
from .admin_views.documents import (
    get_categories,
    get_chapters,
    get_subjects,
    post_document_from_word,
    post_document_from_content
)
from .user_views.documents import (
    get_tree_by_subject,
    get_lesson,
    get_audio,
)

from .admin_views.chats import (
    post_answer_train,
)

from .user_views.chats import (
    get_chat,
)

urlpatterns = [
    # Document
    path("document/categories/", get_categories),
    path("document/chapters/", get_chapters),
    path("document/subjects/", get_subjects),

    path("document/gettree/", get_tree_by_subject, name="document_gettree"),
    path("document/lesson/audio/", get_audio, name="document_lesson_audio"),
    path("document/lesson/", get_lesson, name="document_lesson"),
    path("document/from/word/", post_document_from_word),
    path("document/from/content/", post_document_from_content),
    # Answer
    path("answer/train/", post_answer_train),
    # Consulting
    path("chat/", get_chat, name="consulting_chat"),
]
