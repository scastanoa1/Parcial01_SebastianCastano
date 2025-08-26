from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def create_flight(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vuelo registrado correctamente.")
            return redirect("flights:list")
        messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = FlightForm()
    return render(request, "flights/form.html", {"form": form})

def list_flights(request: HttpRequest) -> HttpResponse:
    flights = Flight.objects.all() 
    return render(request, "flights/list.html", {"flights": flights})

def stats(request: HttpRequest) -> HttpResponse:
    count_national = Flight.objects.filter(type="Nacional").count()
    count_international = Flight.objects.filter(type="Internacional").count()
    agg = Flight.objects.filter(type="Nacional").aggregate(avg=Avg("price"))
    avg_national = agg.get("avg") 
    context = {
    "count_national": count_national,
    "count_international": count_international,
    "avg_national": avg_national,
    }
    return render(request, "flights/stats.html", context)