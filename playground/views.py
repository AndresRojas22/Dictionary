from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import wordForm

# Create your views here.
def SayHello(request):
    return HttpResponse("Hello World")

def Home(request):
    return render(request,'home.html')

def word(request):
    if request.method == "POST":
        form = wordForm(request.POST)
        
        if form.is_valid():
            return render(request, "definition.html", {"word": form.cleaned_data['word']})
    else:
        form = wordForm()
    return render(request, "home.html",{"form": form})