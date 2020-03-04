# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=120)
    author = models.CharField(max_length=120)

    def __str__(self):
        return self.objects.values_list()