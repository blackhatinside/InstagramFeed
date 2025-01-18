# InstagramFeed\social\urls.py

from django.urls import path
from .views import (
    AuthorList, AuthorDetail,
    PostList, PostDetail,
    CommentList, CommentDetail,
    AuthorPosts, AuthorComments,
    PostComments
)

urlpatterns = [
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
    path('authors/<int:pk>/posts/', AuthorPosts.as_view()),
    path('authors/<int:pk>/comments/', AuthorComments.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/<int:pk>/comments/', PostComments.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]

