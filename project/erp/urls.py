from . import views
from django.urls import path



app_name = 'erp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('show', views.show, name = 'show'),
    path('register', views.register, name = 'register')
]

