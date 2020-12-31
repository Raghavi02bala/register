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


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    my_series = models.CharField(max_length=50)
    due_date = models.DateField()
    number = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=50)
    my_currency = models.CharField(max_length=50)
    conversion_rate = models.DecimalField(max_digits=20, decimal_places=5)
    gst_type_of_dealer = models.IntegerField()
    gst_reverse_charge = models.BooleanField()
    gst_ecomm_gstin = models.CharField(max_length=50)
    gst_recepient_name = models.CharField(max_length=30)
    gst_my_state = models.CharField(max_length=30)
    gstin = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=50)
    gst_port_code =  models.CharField(max_length=7)
    gst_shipping_bill_number = models.IntegerField()
    gst_shipping_bill_date = models.DateField()

    class Document(models.IntegerChoices):
        Sales = 1
        Sales_Order = 2
        Sales_Challan = 3
        Purchase = 4
        Purchase_Order = 5
        Purchase_Challan = 6

    gst_nature_of_document = models.IntegerField(choices=Document.choices)

    class Transaction(models.IntegerChoices):
        Sales_Ttaxable = 1
        Sales_Exempted = 2
        Sales_Non_Gst = 3
        Exports_Exempted = 4
        Purchases_Zero_Rated = 5
        Imports_Taxable = 6 

    gst_nature_of_transaction = models.IntegerField(choices=Transaction.choices)
    is_cancelled = models.BooleanField()
    amount = models.DecimalField(max_digits=20, decimal_places=5)
    party_bill_number = models.CharField(max_length=30)
    party_bill_date = models.DateField()
    class Tax_Scope(models.IntegerChoices):
        Exclusive_Of_Tax = 0
        Inclusive_Of_Tax = 1
        Out_Of_Scope = 3 
    tax_scope = models.IntegerField(choices=Tax_Scope.choices)
    my_account = models.CharField(max_length=30)
    my_center = models.CharField(max_length=30)


class VoucherItemRow(models.Model):
    my_purchase = models.ForeignKey('Purchase',on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    my_item = models.CharField(max_length=20)
    my_umo = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=40,decimal_places=5)
    price = models.DecimalField(max_digits=10,decimal_places=5)
    lot_no = models.IntegerField()
    description = models.CharField(max_length=50)
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    amount = models.DecimalField(max_digits=20,decimal_places=5)
    effective_amount = models.DecimalField(max_digits=20,decimal_places=5)
    taxable_amount = models.DecimalField(max_digits=20,decimal_places=5)
    final_amount = models.DecimalField(max_digits=20,decimal_places=5)


class VoucherBillSundaryRow(models.Model):
    my_voucher_item = models.ForeignKey('VoucherItemRow',on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    my_bill_sundry = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=20,decimal_places=5)
    amount = models.DecimalField(max_digits=20,decimal_places=5)
    description = models.CharField(max_length=50)

class SubItemRow(models.Model):
    my_voucher_item = models.ForeignKey('VoucherItemRow',on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    quantity = models.DecimalField(max_digits=20,decimal_places=5)
    serial_number = models.IntegerField()
    description = models.CharField(max_length=50)

    