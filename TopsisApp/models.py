from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django import forms

# Create your models here.


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
