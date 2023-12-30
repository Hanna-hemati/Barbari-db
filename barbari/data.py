# Import necessary modules
from faker import Faker
from .models import Driver, Cargo

# Create a Faker instance
faker = Faker()

# Number of fake records you want to create
num_records = 10


for _ in range(num_records):
    cargo_instance = Cargo.objects.order_by('?').first()  # Get a random Cargo instance

    driver = Driver(
        cargo=cargo_instance,
        name=faker.name(),
        license_plate_number=fake.isbn10(),
        capacity=faker.random_int(min=1, max=100),
    )
    driver.save()

print(f'Successfully populated {num_records} Driver records')

for _ in range(10):
    cargo_instance = Cargo.objects.order_by('?').first()
    driver = Driver(
        cargo=cargo_instance,
        name=faker.name(),
        license_plate_number=faker.isbn10(),
        capacity=faker.random_int(min=1, max=100),
         )
    driver.save()