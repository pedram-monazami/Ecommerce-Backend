from django.contrib import admin

from .models import *


class AddressShow(admin.ModelAdmin):
    """
    Customizing appearance of addresses on admin panel.
    """
    list_filter = ['country', 'city']
    search_fields = ['street', 'zipcode']
    ordering = ['country']
    list_per_page = 15


class CustomerShow(admin.ModelAdmin):
    """
    Customizing appearance of customers on admin panel.
    """
    list_display = ['user', 'phone', 'name']
    search_fields = ['user', 'phone', 'name']
    ordering = ['user', ]
    list_per_page = 15


# Registering models to admin panel
admin.site.register(Address, AddressShow)
admin.site.register(Customer, CustomerShow)
