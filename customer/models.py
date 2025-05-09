from django.db import models

from core.models import BaseModel, User


class Customer(BaseModel):
    """
    The customer model.
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='No Name', help_text="Customer name", null=True, blank=True)
    email = models.EmailField(max_length=50, default="ex@2xample.com", null=False, help_text="Customer email",
                              blank=True)
    phone = models.CharField(max_length=16, default="09122222222", null=False, help_text="Customer phone number",
                             blank=True)
    password = models.CharField(max_length=32, default="111", help_text="Customer password", null=True, blank=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'Name: {self.name}'


class Address(BaseModel):
    """
    The address model
    """
    country = models.CharField(max_length=50, default='Country', help_text="Country name")
    city = models.CharField(max_length=50, default='City', help_text="City name")
    street = models.CharField(max_length=200, default='Address', help_text="Full Address")
    zipcode = models.CharField(default='1111111111', help_text="Zip Code", max_length=11, null=True, blank=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'Address: {self.street} , {self.city} , {self.country} Postal Code: {self.zipcode}'

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
