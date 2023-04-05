from . import views
from django.urls import path



app_name = 'erp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('show', views.show, name = 'show'),
    path('registerform', views.register_form, name = 'register_form'),
    path('registerdb', views.register_db, name = 'register_db')
]

