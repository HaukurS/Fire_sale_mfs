from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from items.models import ItemBid


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Notification(models.Model):
    name = models.CharField(max_length=255, null=True)
    item_bid = models.ForeignKey(ItemBid, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
