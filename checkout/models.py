from django.db import models
from Users.models import Profile


class PaymentInfo(models.Model):
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    exp_date = models.DateField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)


