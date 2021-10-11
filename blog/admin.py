from django.contrib import admin
from .models import BlogPost, BlogComment


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Blog posts """

    list_display = (
        'author',
        'date',
        'blog_title',
        'blog_intro',
        'blog_content'
    )


class BlogCommentAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Blog Comments """
    list_display = (
        'blogpost',
        'comment',
        'user'
    )


admin.site.register(BlogPost)
admin.site.register(BlogComment, BlogCommentAdmin)
