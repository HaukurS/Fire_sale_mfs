from django.db import models


# Create your form here.


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=9999, blank=True, null=True)

    def __str__(self):
        return self.name


