from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def taskList(request):
    return HttpResponse('To do list')
