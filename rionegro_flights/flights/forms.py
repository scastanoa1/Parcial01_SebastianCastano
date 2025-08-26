from decimal import Decimal
from django import forms
from .models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["name", "type", "price"]
        widgets = {"type": forms.Select(choices=Flight.TYPE_CHOICES)}
        labels = {"name": "Nombre", "type": "Tipo", "price": "Precio"}


    def clean_name(self):
        name: str = self.cleaned_data.get("name", "").strip()
        if not name:
            raise forms.ValidationError("El nombre es obligatorio.")
        return name


    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None or price <= Decimal("0"):
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return price