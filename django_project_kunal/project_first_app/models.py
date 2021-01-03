from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.last_name


class DriverIdentity(models.Model):
    driver = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number_identification = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()

    def __str__(self):
        return self.driver.last_name


class Car(models.Model):
    number_guest = models.CharField(max_length=15)
    marks = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.model


class Possession(models.Model):
    owner = ForeignKey(CarOwner, on_delete=models.CASCADE,
                       related_name='owner')
    car = ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.owner.last_name
