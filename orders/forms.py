from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Электронная почта"
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес"}))

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "address",)
