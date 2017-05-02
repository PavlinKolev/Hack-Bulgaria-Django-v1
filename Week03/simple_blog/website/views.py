from django.shortcuts import render, reverse, redirect
from django.http import Http404
from website.models import Tag, Comment, BlogPost
from website.forms import BlogPostForm


def index(request):
    blogs = BlogPost.objects.all()
    return render(request, 'index.html', locals())


def detail(request, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
        return render(request, 'detail_blog_post.html', locals())
    except BlogPost.DoesNotExist:
        raise Http404("No blog post with this id.")


def create_blog(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']
            blog = BlogPost.objects.create(title=title, content=content)
            [blog.tags.add(tag) for tag in tags]
            return redirect(reverse('website:index'))
        else:
            return render(request, 'create_blog_post.html', {'form': form})
    return render(request, 'create_blog_post.html', {'form': form})
