from django.contrib import admin
from .models import Flight

# Register your models here.

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "price")
    list_filter = ("type",)
    search_fields = ("name",)