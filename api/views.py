from django.shortcuts import render
from .models import Employee,Enterprise
from .serializers import EmployeeSerializer,EnterpriseSerializer
from rest_framework import generics

class EnterpriseCreateList(generics.CreateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class EmployeeCreateList(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
