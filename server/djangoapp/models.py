# Uncomment the following imports before adding the Model code
import uuid

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    mfgr = models.CharField(max_length=100)
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    ) 

    def __str__(self):
        return f'{self.name}'


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('GREMLIN', 'Gremlin'),
        ('TRUCK', 'Truck'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('SPORTS', 'Sports')
    ]
    model_type = models.CharField(max_length=15, choices=CAR_TYPES, default='TRUCK')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2199),
            MinValueValidator(1100)
        ]
    )
    wheel_count = models.IntegerField(
        default=4,
        validators=[
            MaxValueValidator(201),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f'{self.car_make.name} - {self.name}'
