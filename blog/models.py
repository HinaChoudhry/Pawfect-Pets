from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    blog_title = models.CharField(max_length=254, null=True, blank=True)
    blog_intro = models.CharField(max_length=254, null=True, blank=True)
    blog_content = models.TextField()
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.blog_title


class BlogComment(models.Model): 
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=1000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment