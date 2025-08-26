from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Flight(models.Model):
    TYPE_CHOICES = [
        ("Nacional", "Nacional"),
        ("Internacional", "Internacional"),
    ]


    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))])


    class Meta:
        ordering = ["price"] 
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"


    def __str__(self) -> str: 
        return f"{self.name} ({self.type}) - ${self.price}"