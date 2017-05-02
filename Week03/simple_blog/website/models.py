from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author_email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')

    def __str__(self):
        return self.title

    def tags_as_str(self):
        return ' '.join([tag.name for tag in self.tags.all()])
