from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post
# Create your views here.
from datetime import datetime

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())


def show_post(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except Exception as e:
        print(e)
        return redirect('/mysite')