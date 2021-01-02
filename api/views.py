from django.shortcuts import render
from .models import Employee,Enterprise,Purchase
from .serializers import EmployeeSerializer,EnterpriseSerializer,Employee_Serializer, PurchaseSerializer
from rest_framework import generics

class EnterpriseCreateList(generics.CreateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class EmployeeCreateList(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EnterpriseList(generics.ListAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class Enterpriseurd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class Employeeurd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class Employee_CreateList(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer

class Purchase_CreateList(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    def get_serializer_context(self):
        return self.request.data

class Purchase_List(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer 

class Purchase_Urd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer