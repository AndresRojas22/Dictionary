from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def SayHello(request):
    return HttpResponse("Hello World")

def Home(request):
    return render(request,'home.html')
