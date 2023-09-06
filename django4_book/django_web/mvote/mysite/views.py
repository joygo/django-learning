from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出了")
    return redirect('/')
