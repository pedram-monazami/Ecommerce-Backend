# Register your models here.
from django.contrib import admin

from landing.models import *


class LocationShow(admin.ModelAdmin):
    """
    Customizing appearance of ShopLocations on admin panel.
    """
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 15


class ContactShow(admin.ModelAdmin):
    """
    Customizing appearance of ContactLocations on admin panel.
    """
    list_display = ['sender_email', 'subject', 'shortened_content', 'location', 'create_datetime']
    filter_fields = ['location']
    search_fields = ['subject', 'content']
    list_per_page = 15

    def shortened_content(self, obj):
        return obj.content[:20] + "..."
    shortened_content.short_description = "content"


admin.site.register(Location, LocationShow)
admin.site.register(Contact, ContactShow)
