from django.contrib import admin
from django.urls import path
from .views import EnterpriseCreateList,EmployeeCreateList

urlpatterns = [
    path('create_enterprise', EnterpriseCreateList.as_view()),
    path('create_employee', EmployeeCreateList.as_view())
] 