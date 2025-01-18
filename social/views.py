# InstagramFeed\social\views.py

from rest_framework import generics
from .models import Author, Post, Comment
from .api.serializers import AuthorSerializer, PostSerializer, CommentSerializer
from .tasks import notify_new_comment

# Handles POST to create new authors
# class AuthorList(generics.CreateAPIView):
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Handles GET/PUT/PATCH/DELETE for existing authors
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# class PostList(generics.CreateAPIView):
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class CommentList(generics.CreateAPIView):
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # Add triggering
    def perform_create(self, serializer):
        comment = serializer.save()
        # Trigger async task
        notify_new_comment.delay(
            comment.post.title,
            comment.author.name,
            comment.content
        )

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# CUSTOM ENDPOINTS/ACTIONS
class AuthorPosts(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author_id=self.kwargs['pk'])

class AuthorComments(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(author_id=self.kwargs['pk'])

class PostComments(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'])