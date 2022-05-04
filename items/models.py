from django.db import models
from Users.models import User


# Create your form here.


class ItemCategory(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=9999)
    condition = models.CharField(max_length=9999)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class ItemImage(models.Model):
    image = models.CharField(max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class ItemOffer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
