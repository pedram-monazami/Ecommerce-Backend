from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    """
    Customizing users on admin panel.
    """
    list_display = ['username', 'first_name', 'last_name', ]
    search_fields = ['username', 'first_name', 'last_name', ]
    list_per_page = 15


admin.site.register(User, UserAdmin)
# Registering models to admin panel
