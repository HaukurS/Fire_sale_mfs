from django.db import models
from django.contrib.auth.models import User
from Users.models import Profile


# Create your form here.


class ItemCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=9999)
    condition = models.CharField(max_length=9999)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    image = models.CharField(max_length=9999, blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    image = models.CharField(max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class ItemBid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item_price = models.FloatField()
    bidder = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    seen = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

