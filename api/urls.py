from django.contrib import admin
from django.urls import path
from .views import (
EnterpriseCreateList,
EmployeeCreateList,
EnterpriseList,
EmployeeList,
Enterpriseurd,
Employeeurd,
Employee_CreateList,
Purchase_CreateList,
Purchase_List,
Purchase_Urd
)

urlpatterns = [
    path('create_enterprise', EnterpriseCreateList.as_view()),
    path('create_employee', EmployeeCreateList.as_view()),
    path('list_enterprise', EnterpriseList.as_view()),
    path('list_employee', EmployeeList.as_view()),
    path('urd_enterprise/<uuid:pk>', Enterpriseurd.as_view()),
    path('urd_employee/<uuid:pk>', Employeeurd.as_view()),
    path('employee_enterprise', Employee_CreateList.as_view()),
    path('purchase', Purchase_CreateList.as_view()),
    path('purchaselist',Purchase_List.as_view()),
    path('purchaseurd/<uuid:pk>', Purchase_Urd.as_view())
] 