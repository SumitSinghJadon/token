from .models import Company
from .models import student
from .serializers import CompanySerializer
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser



class Company(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    

class Student(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    

    