from .views import combined_list, drivers_within_capacity, cargo_search
from django.urls import path

urlpatterns = [
    path('', combined_list, name='combined_list'),
    path('driver/<int:capacity>/', drivers_within_capacity, name='drivers_within_capacity'),
    path('cargo-search/', cargo_search, name='cargo_search'),
]
