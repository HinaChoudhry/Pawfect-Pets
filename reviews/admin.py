from django.contrib import admin
from .models import Review


class ReviewInline(admin.TabularInline):
    """ Allows view/edit of reviews from Product detail page """
    model = Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'product',
        'user',
        'date',
    )
