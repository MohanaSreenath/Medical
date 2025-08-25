from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'home.html')

def hello(request):
    name = request.GET.get('name','Guest')
    return render(request, 'home.html', {'name': name})
def hello2(request , name):
    return render(request, 'home.html', {'name': name})

