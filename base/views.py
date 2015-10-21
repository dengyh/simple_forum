from django.shortcuts import render
from common.mako import render

# Create your views here.

def index_view(request, templateName):
    return render(templateName)