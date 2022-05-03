from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse('<h1>Hello from the index view in the Profile app</h1>')