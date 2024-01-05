from django.shortcuts import render
from django.http import HttpResponse
from .forms import wordForm
import requests

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

def search(request):
    if request.method == 'POST':
        input_value = request.POST.get('word')
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{input_value}'
        
        print(f"Realizando API call a: {url}")
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            first_example = None
            if data and 'meanings' in data[0]:
                for definition in data[0]['meanings'][0]['definitions']:
                    if 'example' in definition and definition['example']:
                        first_example = definition['example']
                        break
                    
            return render(request, "definition.html", {"data":data, "first_example": first_example})
        else:
            return render(request, "definition.html",{"error_message":"Definition not found :("})
    return render(request, "home.html")
            