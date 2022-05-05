from django.db import models
from Users.models import User


# Create your models here.
class ContactInfo(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PaymentInfo(models.Model):
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    exp_date = models.DateTimeField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
