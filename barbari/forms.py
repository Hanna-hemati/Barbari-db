from django import forms
from .models import Cargo, Driver, ChickenCo, PoultryFarmers

class CargoSearchForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['driver_name']

    def search(self):
        print('cargo search')
        driver_name = self.data.get('driver_name')
        print(f"the driver name is {driver_name}")
        return Driver.objects.filter(name__contains=driver_name)

class CargoFilterForm(forms.ModelForm):

    class Meta:
        model = Cargo
        fields = ['quantity']

    def search(self):
        min_quantity = self.cleaned_data.get('quantity')
        print(f"The minimum quantity is {min_quantity}")
        return Cargo.objects.filter(quantity__gte=min_quantity)


class DriverSearchForm(forms.ModelForm):  
    class Meta:
        model = Driver
        fields = ['name']

    def search(self):
        name = self.cleaned_data.get('name')
        return self.Meta.model.objects.filter(name__icontains=name)

class ChickenCoSearchForm(forms.ModelForm):
    class Meta: 
        model = ChickenCo
        fields = ['name']

    def search(self):
        name = self.cleaned_data.get('name')
        return self.Meta.model.objects.filter(name__icontains=name)

class PoultryFarmersSearchForm(forms.ModelForm):
    class Meta:
        model = PoultryFarmers
        fields = ['name']
    
    def search(self):
        name = self.cleaned_data.get('name')
        return self.Meta.model.objects.filter(name__icontains=name)