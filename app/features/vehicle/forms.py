from .models import Vehicle
from django import forms

class VehicleForm(forms.Form):
    model = forms.CharField(widget=forms.TextInput(attrs={'id': 'vehicle-model'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'id': 'vehicle-price', 'min': '30000'}),initial=100000.00)
    year_make = forms.CharField(widget=forms.TextInput(attrs={'id': 'vehicle-year_make'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'id': 'vehicle-number'}))

    class Meta:
        model = Vehicle
        fields = ["model", "number", "year_make", "price"]