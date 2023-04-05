from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import Employee, Job



def index(request):
    job = Job.objects.count()
    employee = Employee.objects.count()
    return render(request, 'erp/index.html', {'job': job,
                                              'employee':employee})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'erp/show.html', {'list_employees': employees,
                                             'null_message': employees.count() == 0})


def register_form(request):
    jobs = Job.objects
    return render(request, 'erp/register.html', {'jobs':jobs})


def register_db(request):
    try:
        data = request.POST
        job = Job.objects.get(pk = data['job'])
    except:
        return render(request, 'erp/register.html', {'error_message': 'Error en el formulario'})
    else:
        job.employee_set.create(name_employee = data['user'], age = data['age'], email = data['email'])
        return HttpResponse('Todo bien...')


