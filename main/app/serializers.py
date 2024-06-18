# from django.contrib.auth.models import User
from .models import Company
from .models import student
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id","Emp_name","Emp_salary","Emp_contact","Emp_Address"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ["id","stu_name","stu_fees","stu_contact","stu_Address"]
