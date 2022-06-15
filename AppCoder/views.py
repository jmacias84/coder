from django.shortcuts import render
from django.http import HttpResponse
from .models import family

def inicio(request):
    return HttpResponse("Bienvenido a mi página")

def familia(request):
    data_familia = family.objects.all()
    print(data_familia)
    return render(request,'paginas/familia.html')

# Create your views here.
