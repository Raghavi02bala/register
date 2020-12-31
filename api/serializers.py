from rest_framework import serializers
import uuid
from .models import Enterprise, Employee, Purchase, VoucherItemRow, VoucherBillSundaryRow, SubItemRow
from phonenumber_field.modelfields import PhoneNumberField

class EnterpriseSerializer(serializers.ModelSerializer):
        id = serializers.UUIDField(default=uuid.uuid4)
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
    id = serializers.UUIDField(default=uuid.uuid4)
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

class Employee_Serializer(serializers.ModelSerializer):
    my_enterprise = EnterpriseSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'email', 'first_name', 'last_name', 'mobile_no', 'password', 
        'my_enterprise']

    def create(self, validated_data):
        enterprise_data = validated_data.pop('my_enterprise')
        enterprise = Enterprise.objects.create(**enterprise_data)
        employee = Employee.objects.create(my_enterprise = enterprise,**validated_data)
        return employee



class VoucherBillSundaryRowSerializer(serializers.ModelSerializer):
    my_voucher_item = serializers.PrimaryKeyRelatedField(queryset=VoucherItemRow.objects.all())
    id = serializers.UUIDField(default=uuid.uuid4)
    my_bill_sundry = serializers.CharField(max_length=30)
    value = serializers.DecimalField(max_digits=20,decimal_places=5)
    amount = serializers.DecimalField(max_digits=20,decimal_places=5,max_value=0)
    description = serializers.CharField(max_length=50)

    class Meta:
        model = VoucherBillSundaryRow
        fields = ['id', 'my_bill_sundry', 'value', 'amount', 'description']

    def validate(self, data):
        if data['amount'] != data['value']:
            raise serializers.ValidationError('Amount should be equal to value')
        return data
######################################################################################

class SubItemRowSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    quantity = serializers.DecimalField(max_digits=20,decimal_places=5)
    serial_number = serializers.IntegerField()
    description = serializers.CharField(max_length=50)

    class Meta:
        model = SubItemRow
        fields = ['id', 'quantity', 'serial_number', 'description']

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError('Quantity should be greater than zero')
        return value 

###########################################################################################
class VoucherItemRowSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    my_item = serializers.CharField(max_length=20)
    my_umo = serializers.CharField(max_length=20)
    quantity = serializers.DecimalField(max_digits=20,decimal_places=5)
    price = serializers.DecimalField(max_digits=20,decimal_places=5)
    lot_no = serializers.IntegerField()
    description = serializers.CharField(max_length=50)
    manufacturing_date = serializers.DateField()
    expiry_date = serializers.DateField()
    amount = serializers.DecimalField(max_digits=20,decimal_places=5,min_value=0)
    effective_amount = serializers.DecimalField(max_digits=20,decimal_places=5,min_value=0)
    taxable_amount = serializers.DecimalField(max_digits=20,decimal_places=5,min_value=0)
    final_amount = serializers.DecimalField(max_digits=20,decimal_places=5,min_value=0)

    voucherbillsundaryrow_set = VoucherBillSundaryRowSerializer(many=True)
    subitemrow_set = SubItemRowSerializer(many=True)

    class Meta:
        model = VoucherItemRow
        fields = ['id', 'my_item', 'my_umo', 'quantity', 
        'price', 'lot_no', 'description', 'manufacturing_date', 'expiry_date', 'amount',
        'effective_amount', 'taxable_amount', 'final_amount', 'voucherbillsundaryrow_set', 
        'subitemrow_set']

    def validate(self, data):
        print(self.context['tax_scope'])
        # print(data)
        if data['quantity'] < 0:
            raise serializers.ValidationError('Quantity should be greater than 0')
        if data['price'] < 0:
            raise serializers.ValidationError('Price should be greater than zero')
        if data['amount'] != data['price']*data['quantity']:
            raise serializers.ValidationError('Calculation mistake')
        if len(data['subitemrow_set']) > 0:
            def myfunc(a):
                # print(a['quantity'])
                return a['quantity']
                
            x = map(myfunc, data['subitemrow_set'])
            # print(x)
            y = sum(x)
            # print(y,data['quantity'])
            if y != data['quantity']:
                raise serializers.ValidationError('Quantity should be sum of all sub item row Quantity')
        if data['expiry_date'] <= data['manufacturing_date']:
            raise serializers.ValidationError('Expiry data should be greater than Manufacturing date')
        return data
#####################################################################################


class  PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    my_series = serializers.CharField(max_length=50)
    due_date = serializers.DateField()
    number = serializers.IntegerField()
    date = serializers.DateField()
    description = serializers.CharField(max_length=50)
    my_currency = serializers.CharField(max_length=50)
    conversion_rate = serializers.DecimalField(max_digits=20, decimal_places=5)
    gst_type_of_dealer = serializers.IntegerField()
    gst_reverse_charge = serializers.BooleanField()
    gst_ecomm_gstin = serializers.CharField(max_length=50)
    gst_recepient_name = serializers.CharField(max_length=30)
    gst_my_state = serializers.CharField(max_length=30)
    gstin = serializers.CharField(max_length=50)
    shipping_address = serializers.CharField(max_length=50)
    billing_address = serializers.CharField(max_length=50)
    gst_port_code =  serializers.CharField(max_length=7)
    gst_shipping_bill_number = serializers.IntegerField()
    gst_shipping_bill_date = serializers.DateField()
    gst_nature_of_document = serializers.ChoiceField(choices=Purchase.Document.choices)
    gst_nature_of_transaction = serializers.ChoiceField(choices=Purchase.Transaction.choices)
    is_cancelled = serializers.BooleanField()
    amount = serializers.DecimalField(max_digits=20, decimal_places=5)
    party_bill_number = serializers.CharField(max_length=30)
    party_bill_date = serializers.DateField()
    tax_scope = serializers.ChoiceField(choices=Purchase.Tax_Scope.choices)
    my_account = serializers.CharField(max_length=30)
    my_center = serializers.CharField(max_length=30)

    voucheritemrow_set = VoucherItemRowSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ['id', 'my_series', 'due_date', 'number', 'date', 'description', 'my_currency',
        'conversion_rate', 'gst_type_of_dealer', 'gst_reverse_charge', 'gst_ecomm_gstin',
        'gst_recepient_name', 'gst_my_state', 'gstin', 'shipping_address', 'billing_address',
        'gst_port_code', 'gst_shipping_bill_number', 'gst_shipping_bill_date', 'gst_nature_of_document',
        'gst_nature_of_transaction', 'is_cancelled', 'amount', 'party_bill_number', 'party_bill_date',
        'tax_scope', 'my_account', 'my_center', 'voucheritemrow_set']  

    def create(self, validated_data):
        return Purchase()
    def validate(self,data):
        # print(data)
        return data

        

   
  
############################################################################################
