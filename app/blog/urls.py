from django.urls import path

from . import views

urlpatterns = [
    # this renders the view home from views file
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
    # name is the name of the path
]
