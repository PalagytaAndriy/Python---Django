from django import forms
from django.core.validators import RegexValidator

class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефону повинен бути введений в форматі: '+9999999999'. До 15 цифр доступно.")
    customer_email = forms.EmailField()
    address = forms.CharField(max_length=200)
    customer_phone = forms.CharField(max_length=20)