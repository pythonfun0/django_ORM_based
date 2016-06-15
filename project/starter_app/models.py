# -*- coding: utf-8 -*-
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField()
	content = models.TextField()
	date_of_creation = models.DateTimeField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_of_creation']
