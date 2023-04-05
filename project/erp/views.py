from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import Employee, Job



def index(request):
    job = Job.objects.count()
    return render(request, 'erp/index.html', {'job': job})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'erp/show.html', {'list_employees': employees,
                                             'null_message': employees.count() == 0})


def register_form(request):
    questions = ('Nombre', 'Edad', 'Correo', )
    return render(request, 'erp/register.html', {})


def register_db(request, name_employee):
    return HttpResponse(f'Has registrado a {name_employee}')


