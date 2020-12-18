import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Enterprise(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=50)
    alias_name =  models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    office_number = PhoneNumberField()
    bill_sundry_decimal_places = models.IntegerField()
    quantity_decimal_places = models.IntegerField()
    currency_decimal_places = models.IntegerField()
    search_vector = models.CharField(max_length=30)
    date_format = models.IntegerField()
    date_separator = models.IntegerField()

class Employee(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    email = models.EmailField(max_length=300)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_no = PhoneNumberField()
    password = models.CharField(max_length=15)
    my_enterprise = models.ForeignKey('Enterprise', on_delete=models.CASCADE)