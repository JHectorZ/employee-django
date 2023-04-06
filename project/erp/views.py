from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
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


def register_job(request):
    return render(request, 'erp/register_job.html',{})


def register_job_db(request):
    data = request.POST
    try:
        job = Job(name_job = data['name'], description = data['description'])
    except (KeyError):
        return render(request, 'erp/register_job.html', {'error_message':'Error en el formulario'})
    else:
        job.save()
        return HttpResponseRedirect(reverse('erp:index'))
    
    
def register_form(request):
    jobs = Job.objects.all
    return render(request, 'erp/register.html', {'jobs':jobs})


def register_db(request):
    try:
        data = request.POST
        job = Job.objects.get(pk = data['job'])
    except:
        return render(request, 'erp/register.html', {'error_message': 'Error en el formulario'})
    else:
        job.employee_set.create(name_employee = data['user'].title(), age = data['age'], email = data['email'])
        return HttpResponseRedirect(reverse('erp:index'))
