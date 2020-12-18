from rest_framework import serializers
from .models import Enterprise,Employee

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ['id', 'name', 'alias_name', 'address', 'office_number', 
        'bill_sundry_decimal_places', 'quantity_decimal_places', 'currency_decimal_places',
        'search_vector', 'date_format', 'date_separator']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'email', 'first_name', 'last_name', 'mobile_no', 'password', 
        'my_enterprise']
        
