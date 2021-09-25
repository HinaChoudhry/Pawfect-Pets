from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('add_blog_post/', views.add_blog_post, name="add_blog_post"),
]