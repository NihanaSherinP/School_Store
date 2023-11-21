# orders/forms.py

from django import forms
from django.core.validators import RegexValidator

from .models import Department, Course

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    phone = forms.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,15}$', 'Enter a valid phone number.')])
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    purpose = forms.ChoiceField(choices=[('enquiry', 'For Enquiry'), ('place_order', 'Place Order'), ('return', 'Return')])
    materials_provide = forms.MultipleChoiceField(choices=[('notebook', 'Debit Note Book'), ('pen', 'Pen'), ('exam_papers', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)
