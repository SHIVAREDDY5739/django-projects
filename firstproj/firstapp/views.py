from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def firstview(request):
    return HttpResponse("<h1>this is my first app</h1>")