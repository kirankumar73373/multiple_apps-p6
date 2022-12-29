from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def keerthi(request):
    return HttpResponse('<h1>keerthi is most pretiest girl</h1>')

def satya(request):
    return HttpResponse('<marquee>satya is the most cunning girl</marquee>')