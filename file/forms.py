from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Brand_Master, Department, IT_Purchase, Item_Master, Opening_Stock, Purchase_Receiving, RequisitionForm, Issued_to, User_Master, Vendor_Master

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","last_name", "username","email","password1", 'password2']

class Opening_Stock_form(ModelForm):
    class Meta:
        model = Opening_Stock
        fields = ["item", "brand","item_model", "capacity", "version", "item_location","qty"]

class UserRequisitionForm(ModelForm):
    class Meta:
        model = RequisitionForm
        fields = ["user", "department", "item", "capacity", "version","qty", "item_image"]

class IT_Purchase_form(ModelForm):
    class Meta:
        model = IT_Purchase
        fields = ["brand", "item_model", "item_serial_number", "Vendor", "warranty_period", "item_location", "purchase_qty", "req", "price"]
        
class Item_Receiving_Form(ModelForm):
    class Meta:
        model = Purchase_Receiving
        fields = ["pur",'Bill_No', 'rec_qty','purchase_price']

class Purchase_Issue_Item_Form(ModelForm):
    class Meta:
        model = Issued_to
        fields = ["purchase", "Users", "issue_qty"]


class Stock_Issue_Item_Form(ModelForm):
    class Meta:
        model = Issued_to
        fields = ["O_stock", "Users",  "issue_qty"]

class User_Add_Form(ModelForm):
    class Meta:
        model = User_Master
        fields = "__all__"

class Item_Master_Form(ModelForm):
    class Meta:
        model = Item_Master
        fields = "__all__"

class Vendor_Master_Form(ModelForm):
    class Meta:
        model = Vendor_Master
        fields = "__all__"
    
class Brand_Master_Form(ModelForm):
    class Meta:
        model = Brand_Master
        fields = "__all__"

class Department_Master_Form(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"