from django.shortcuts import render
from django.http import HttpResponse
from .models import family

def inicio(request):
    return HttpResponse("Bienvenido a mi página")

def familia(request):
    familiares = family.objects.all()
    #print(familiares)
    return render(request,'paginas/familia.html',{'familiares': familiares})

# Create your views here.
