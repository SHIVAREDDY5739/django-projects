from django.shortcuts import render

# Create your views here.
def firsthtmltemp(request):
    return render(request, 'templateapp/index.html')

def secondhtmltemp(request):
    return render(request, 'templateapp/class and id.html')