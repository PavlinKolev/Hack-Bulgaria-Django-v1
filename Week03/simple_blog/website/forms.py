from django.forms import ModelForm
from website.models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags']
