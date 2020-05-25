from django.shortcuts import render

from django.http import  HttpResponse

def root(request):
    return HttpResponse("<h1>The Server Started Successfully at ROOT APP..</h1>")