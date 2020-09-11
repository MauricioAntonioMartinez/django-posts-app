from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def home(request):  # the root folder of the templates must be the templates folder
    # pass a context
    return render(request, "blog/home.html", context={"posts": Post.objects.all()})
    # this also populates the data from the user


def about(request):
    return render(request, "blog/about.html", context={"title": "About Page"})
