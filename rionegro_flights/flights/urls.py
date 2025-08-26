from django.urls import path
from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.home, name='home'),
    path("flights/create/", views.create_flight, name="create"),
    path("flights/", views.list_flights, name="list"),
    path("flights/stats/", views.stats, name="stats"),
]