from django.db import models

from core.models import BaseModel


class Location(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_email = models.EmailField(default='default@example.com')

    def __str__(self):
        return self.name


class Contact(BaseModel):
    sender_email = models.EmailField()
    subject = models.CharField(max_length=150)
    content = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
