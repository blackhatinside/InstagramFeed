# InstagramFeed\social\api\serializers.py

from rest_framework import serializers
from ..models import Author, Post, Comment

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		 model = Author
		 # fields = '__all__' # expose all fields
		 fields = ['id', 'name', 'email']

class PostSerializer(serializers.ModelSerializer):
	author_name = serializers.ReadOnlyField(source='author.name')
	comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		 model = Post
		 fields = ['id', 'author', 'author_name', 'title', 'content', 'created_at', 'comments']

class CommentSerializer(serializers.ModelSerializer):
	author_name = serializers.ReadOnlyField(source='author.name')
	post_title = serializers.ReadOnlyField(source='post.title')

	class Meta:
		 model = Comment
		 fields = ['id', 'post', 'post_title', 'author', 'author_name', 'content', 'created_at']

