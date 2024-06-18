from django.contrib import admin
from .models import Company,student

# Register your models here


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['Emp_name','Emp_contact']

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['stu_name','stu_fees']


