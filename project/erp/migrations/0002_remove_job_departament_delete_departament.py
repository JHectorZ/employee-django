# Generated by Django 4.2 on 2023-04-05 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='departament',
        ),
        migrations.DeleteModel(
            name='Departament',
        ),
    ]
