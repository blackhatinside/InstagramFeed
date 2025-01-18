# InstagramFeed\social\models.py

from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Post(models.Model):
	# Post --> Author: 1:1
	# Author --> Post: 1:M
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	# Comment --> Post: 1:1
	# Post --> Comment: 1:M
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.author} : {self.content}"

