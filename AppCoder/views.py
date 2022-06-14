from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido a mi página")

def familia(request):
    return render(request,'paginas/familia.html')

# Create your views here.
