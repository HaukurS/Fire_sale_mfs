from django.db import models


# Create your form here.

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=9999, blank=True, null=True)
    street_name = models.CharField(max_length=999, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


