from django.db import models

# Create your models here.

class Company(models.Model):
    Emp_name = models.CharField(max_length = 50)
    Emp_salary = models.IntegerField()
    Emp_contact = models.IntegerField()
    Emp_Address = models.CharField(max_length = 50)
    
    
class student(models.Model):
    stu_name = models.CharField(max_length = 50)
    stu_fees = models.IntegerField()
    stu_contact = models.IntegerField()
    stu_Address = models.CharField(max_length = 50)
    