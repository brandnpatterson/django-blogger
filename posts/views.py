# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

def posts_view(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)
