# InstagramFeed\social\views.py

from django.shortcuts import render

from rest_framework import viewsets
from .models import Author, Post, Comment
from .api.serializers import AuthorSerializer, PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # GET /authors/1/posts/ → All posts by author ID 1
    @action(detail=True)
    def posts(self, request, pk=None):
        author = self.get_object()
        posts = Post.objects.filter(author=author)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # GET/authors/1/comments/ → All comments by author ID 1
    @action(detail=True)
    def comments(self, request, pk=None):
        author = self.get_object()
        comments = Comment.objects.filter(author=author)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # GET /posts/1/comments/ → All comments under post ID 1
    @action(detail=True)
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer