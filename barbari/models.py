from django.db import models

class Cargo(models.Model):
    class CargoType(models.TextChoices):
        TURKEY = "turkey", ("بوقلمون")
        HEN = "hen", ("مرغ")
        CHICKEN = "checken", ("جوجه")
        EGG = "egg", ("تخم مرغ")
    
    driver_name = models.CharField(max_length=200)  # Added max_length
    quantity = models.IntegerField()
    losses = models.IntegerField()
    cargo_type = models.CharField(
        max_length=10,
        choices=CargoType.choices,
        default=CargoType.TURKEY,
    )

    def __str__(self):
        return self.driver_name

class Driver(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    license_plate_number = models.CharField(max_length=500)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name  # Fixed reference to name

class ChickenCo(models.Model):
    class CargoType(models.TextChoices):
        TURKEY = "turkey", ("بوقلمون")
        HEN = "hen", ("مرغ")
        CHICKEN = "checken", ("جوجه")
        EGG = "egg", ("تخم مرغ")

    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)  # Added null=True
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)  # Added max_length
    cargo_type = models.CharField(
        max_length=10,
        choices=CargoType.choices,
        default=CargoType.TURKEY,
    )

    def __str__(self):
        return self.name

class PoultryFarmers(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)  # Added null=True
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
