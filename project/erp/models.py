from django.db import models
from django.utils import timezone

class Job(models.Model):
    name_job = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 500 )

    def __str__(self):
        return self.name_job


class Employee(models.Model):
    name_employee = models.CharField( max_length = 200 )
    age = models.IntegerField( default = 0)
    email = models.EmailField( max_length = 200 )
    contract_date = models.DateField( default = timezone.now())
    job_status = models.ForeignKey( Job, on_delete = models.SET_NULL, null = True )

    def __str__(self):
        return self.name_employee

