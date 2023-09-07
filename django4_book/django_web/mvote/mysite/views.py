from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mysite import models
# Create your views here.

def index(request):
    all_polls = models.Poll.objects.all().order_by('-created_at')
    paginator = Paginator(all_polls, 5)
    p = request.GET.get('p')

    try:
        polls = paginator.page(p)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    return render(request, 'index.html', locals())