from django.contrib import admin
from .models import Post, Myupload, Employee
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Post)
admin.site.register(Myupload)


# @admin.register(Employee)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'empid', 'name', 'contact', 'email', 'dept', 'doj', 'dob', 'empphoto']


@admin.register(Employee)
class EmployeeModelAdmin(ImportExportModelAdmin):
    list_display = ['id', 'empid', 'name', 'contact', 'email', 'dept', 'doj', 'dob', 'empphoto']
