from django.contrib import admin

from .actions import *
from .models import *


class CategoryShow(admin.ModelAdmin):
    """
    An admin model class for costuming categories on admin panel.
    """
    list_display = ['name', 'discount']
    search_fields = ['name']
    list_per_page = 15


class CommentShow(admin.ModelAdmin):
    """
    An admin model class for costuming comments on admin panel.
    """
    search_fields = ['content']
    list_filter = ['product']
    list_display = ['content', 'product']
    list_per_page = 15


class ProductShow(admin.ModelAdmin):
    """
    An admin model class for costuming products on admin panel.
    """
    list_display = ['name', 'brand', 'price', 'discount']
    search_fields = ['name']
    list_per_page = 15
    actions = [set_is_deleted_true, set_is_active_true, set_is_active_false]
    set_is_deleted_true.short_description = "Set deleted"
    set_is_active_true.short_description = "Set active"
    set_is_active_false.short_description = "Set deactive"


class DiscountShow(admin.ModelAdmin):
    """
    An admin model class for costuming discounts on admin panel.
    """
    list_display = ['description', 'type', 'amount']
    search_fields = ['description']
    list_per_page = 15
    list_filter = ['type']

    actions = [set_is_deleted_true_discount, set_is_active_true_discount, set_is_active_false_discount]
    set_is_deleted_true.short_description = "Set deleted"
    set_is_active_true.short_description = "Set active"
    set_is_active_false.short_description = "Set deactive"


class BrandShow(admin.ModelAdmin):
    """
    An admin model class for costuming brands on admin panel.
    """
    list_display = ['name', 'discount']
    search_fields = ['name']
    list_per_page = 15


admin.site.register(Category, CategoryShow)
admin.site.register(Discount, DiscountShow)
admin.site.register(Brand, BrandShow)
admin.site.register(Comment, CommentShow)
admin.site.register(Product, ProductShow)
# Registering models to admin panel
