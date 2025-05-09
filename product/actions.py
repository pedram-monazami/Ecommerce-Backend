from product.tasks import *


def set_is_deleted_true(modelAdmin, request, queryset):
    ids = list(queryset.values_list('id', flat=True))
    set_is_deleted_true_task(ids)


def set_is_active_false(modelAdmin, request, queryset):
    ids = list(queryset.values_list('id', flat=True))
    set_is_active_false_task(ids)


def set_is_active_true(modelAdmin, request, queryset):
    ids = list(queryset.values_list('id', flat=True))
    set_is_active_true_task(ids)


def set_is_deleted_true_discount(modelAdmin, request, queryset):
    ids = list(queryset.values_list('id', flat=True))
    set_is_deleted_true_discount_task(ids)


def set_is_active_false_discount(modelAdmin, request, queryset):
    ids = list(queryset.values_list('id', flat=True))
    set_is_active_false_discount_task(ids)


def set_is_active_true_discount(modelAdmin, request, queryset):
    ids = list(queryset.values_list('id', flat=True))
    set_is_active_true_discount_task(ids)
