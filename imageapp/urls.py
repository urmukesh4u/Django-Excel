from django.contrib import admin
from django.urls import path
from . import views

app_name = 'imageapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('addimage', views.addimage, name='addimage'),
    path('uploadimage', views.send_files, name='uploadimage'),
    path('addexcel', views.addexcel, name='addexcel'),
    path('uploadexcel', views.excel_upload,name='uploadexcel'),
    path('addemployee', views.addEmployee, name='addemployee'),
    path('viewemp/<int:id>', views.viewEmployee, name='viewemp'),
    path('delete/<int:id>', views.delete, name='delete'),
]
 

 