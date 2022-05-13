from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from items.models import ItemBid


# We don't use this model anymore
class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Notification(models.Model):
    name = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
