from django.shortcuts import redirect
from common.mako import render

from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from account.models import UserProfile

from django.contrib import auth
from django.auth.forms import UserCreationForm

import json

# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request, templateName):
    if request.user.is_authenticated():
        return redirect('/')

    nextPage = request.GET.get('next', '/')
    errMessage = ''

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(nextPage)
        errMessage = '用户名或者密码错误'

    return render(request, templateName, {
        'error': errMessage,
        'next': nextPage,
        })

@require_GET
def logout(request):
    auth.logout(request)
    return redirect('/')

@require_http_methods(['GET', 'POST'])
def register(request, templateName):
    nextPage = request.GET.get('next', '/')
    errMessage = ''

    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password1', None)
        if userForm.is_valid():
            userForm.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(nextPage)
        else:
            errMessage = '注册失败'
    return render(request, templateName, {
        'error': errMessage,
        'next': nextPage,
        })
