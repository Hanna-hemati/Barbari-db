from django.shortcuts import render
from .models import Cargo, Driver, ChickenCo, PoultryFarmers

def cargo_list(request):
    cargo_data = Cargo.objects.all()
    return render(request, 'barbari/cargo_list.html', {'cargo_data': cargo_data})

def driver_list(request):
    driver_data = Driver.objects.all()
    return render(request, 'barbari/driver_list.html', {'driver_data': driver_data})

def chicken_co_list(request):
    chicken_co_data = ChickenCo.objects.all()
    return render(request, 'barbari/chicken_co_list.html', {'chicken_co_data': chicken_co_data})

def poultry_farmers_list(request):
    poultry_farmers_data = PoultryFarmers.objects.all()
    return render(request, 'barbari/poultry_farmers_list.html', {'poultry_farmers_data': poultry_farmers_data})

def combined_list(request):
    cargo_data = Cargo.objects.all()
    driver_data = Driver.objects.all()
    chicken_co_data = ChickenCo.objects.all()
    poultry_farmers_data = PoultryFarmers.objects.all()

    return render(
        request,
        'barbari/combined_list.html',
        {
            'cargo_data': cargo_data,
            'driver_data': driver_data,
            'chicken_co_data': chicken_co_data,
            'poultry_farmers_data': poultry_farmers_data,
        }
    )