from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment
from products.models import Category

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('blog_title', 'blog_intro', 
                'blog_content', 'image',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['blog_title'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'



class BlogCommentForm(forms.ModelForm):
    class Meta: 
        model = BlogComment
        fields = ('comment',)
