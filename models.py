from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)

class Blog_post(models.Model):
    created = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    tags = models.ManytoManyField(Tag)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField('date published')

