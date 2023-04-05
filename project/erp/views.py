from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import Departament, Employee, Job



def index(request):
    departament = Departament.objects.count()
    return render(request, 'erp/index.html', {'departament': departament})


def show(request):
    return HttpResponse("Estas en show")


def register(request):
    return HttpResponse("Estas en registro")


