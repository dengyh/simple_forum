from common.template import render

# Create your views here.

def index_view(request, templateName):
    return render(request, templateName)