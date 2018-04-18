from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse('Hello World! from GOD')
