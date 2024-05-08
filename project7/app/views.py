from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.


def insert_topic(request):
    ETFO = TopicForm()
    d = {'ETFO':ETFO}
    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('DOne')
        else:
            return HttpResponse('Invalid Data')
    return render(request, 'insert_topic.html',d)

def insert_website(request):
    EWFO = WebsiteForm()
    d = {'EWFO':EWFO}
    if request.method == 'POST':
        WFDO = WebsiteForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Done')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_website.html', d)

def insert_access(request):
    EAFO = AccessForm()
    d = {'EAFO':EAFO}
    if request.method == 'POST':
         AFDO = AccessForm(request.POST)
         if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('DOne')
         return HttpResponse('Invalid Data')
    return render(request, 'insert_access.html', d)