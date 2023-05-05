from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def secondview(request):
    return HttpResponse("<h3>this is my second app</h3>")