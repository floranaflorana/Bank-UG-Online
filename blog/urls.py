from django.urls import path
from . import views

# Here we're importing Django's function path and all of our views from the blog application

urlpatterns = [
    path('', views.post_list, name='post_list'),
]