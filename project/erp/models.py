from django.db import models



class Departament(models.Model):
    name_departament = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 500 )


class Job(models.Model):
    name_job = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 500 )
    departament = models.models.ForeignKey( Departament, on_delete = models.CASCADE )


class Employee(models.Model):
    name_employee = models.CharField( max_length = 200 )
    age = models.IntegerField( default = 0)
    email = models.EmailField( max_length = 200 )
    job_status = models.ForeignKey( Job )


