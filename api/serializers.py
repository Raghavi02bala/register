from rest_framework import serializers
import uuid
from .models import Enterprise,Employee
from phonenumber_field.modelfields import PhoneNumberField

class EnterpriseSerializer(serializers.ModelSerializer):
        id = serializers.UUIDField(default=uuid.uuid4,read_only=True)
        name = serializers.CharField(max_length=50)
        alias_name =  serializers.CharField(max_length=30)
        address = serializers.CharField(max_length=200)
        office_number = PhoneNumberField()
        bill_sundry_decimal_places = serializers.IntegerField()
        quantity_decimal_places = serializers.IntegerField()
        currency_decimal_places = serializers.IntegerField()
        search_vector = serializers.CharField(max_length=30)
        date_format = serializers.IntegerField()
        date_separator = serializers.IntegerField()

        class Meta:
            model = Enterprise
            fields = ['id', 'name', 'alias_name', 'address', 'office_number', 
        'bill_sundry_decimal_places', 'quantity_decimal_places', 'currency_decimal_places',
        'search_vector', 'date_format', 'date_separator']


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4,read_only=True)
    email = serializers.EmailField(max_length=300)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    mobile_no = PhoneNumberField()
    password = serializers.CharField(max_length=15)
    my_enterprise = serializers.PrimaryKeyRelatedField(queryset=Enterprise.objects.all())

    class Meta:
        model = Employee
        fields = ['id', 'email', 'first_name', 'last_name', 'mobile_no', 'password', 
        'my_enterprise']

        
