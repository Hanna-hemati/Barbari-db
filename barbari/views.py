from django.shortcuts import render
from .models import Cargo, Driver, ChickenCo, PoultryFarmers
from .forms import CargoSearchForm, DriverSearchForm, ChickenCoSearchForm, PoultryFarmersSearchForm, CargoFilterForm

def cargo_search(request):
    form = CargoSearchForm()
    if request.GET:
        form = CargoSearchForm(request.GET)
        results = form.search() 
        return render(request, 'barbari/search.html', {'form': form, 'results': results})
  
    return render(request, 'barbari/search.html', {'form': form})

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

def drivers_within_capacity(request, capacity):

    min_capacity = int(capacity)
    
    drivers = Driver.objects.filter(capacity__gte=min_capacity)

    context = {
        'drivers': drivers,
        'capacity': min_capacity,
    }

    return render(request, 'barbari/drivers.html', context)

def combined_list(request):

    cargo_data = Cargo.objects.all()
    driver_data = Driver.objects.all() 
    chicken_co_data = ChickenCo.objects.all()
    poultry_farmers_data = PoultryFarmers.objects.all()

    cargo_search_form = CargoSearchForm()
    cargo_filter_form = CargoFilterForm()
    search_results = None
    filtered_cargo_data = None

    if request.GET:
        cargo_search_form = CargoSearchForm(request.GET)
        cargo_filter_form = CargoFilterForm(request.GET)

        if cargo_search_form.is_valid():
            print("search")
            search_results = cargo_search_form.search()

        if cargo_filter_form.is_valid():
            print("here")
            filtered_cargo_data = cargo_filter_form.search()
    

    context = {
        'cargo_data': cargo_data, 
        'driver_data': driver_data,
        'chicken_co_data': chicken_co_data,
        'poultry_farmers_data': poultry_farmers_data,
        'cargo_search_form': cargo_search_form,
        'cargo_filter_form': cargo_filter_form,
        'search_results': search_results,
        'filtered_cargo_data': filtered_cargo_data,
    }
    
    if search_results:
        print(search_results)
        return render(request, 'barbari/search_results.html', {'search_results': search_results})
    elif filtered_cargo_data:
        print(filtered_cargo_data)
        return render(request, 'barbari/filtered_cargo_results.html', {'filtered_cargo_data': filtered_cargo_data})
    
    return render(request, 'barbari/list.html', context)