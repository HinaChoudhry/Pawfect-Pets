from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<int:blogpost_id>/', views.blog_detail, name='blog_detail'),
    path('add_blog_post/', views.add_blog_post, name="add_blog_post"),
    path('edit_blog_post/<int:blogpost_id>/', views.edit_blog_post, name="edit_blog_post"),
    path('delete_blog_post/<int:blogpost_id>/', views.delete_blog_post, name='delete_blog_post'),
    path('add_blog_comment/<int:blogpost_id>/', views.add_blog_comment, name="add_blog_comment"),
    path('edit_blog_comment/<int:blogcomment_id>/<int:blogpost_id>/', views.edit_blog_comment, name='edit_blog_comment'),
]