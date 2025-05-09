from celery import shared_task
from product.models import Product, Discount


@shared_task()
def set_is_deleted_true_task(product_ids):
    products = Product.objects.filter(id__in=product_ids)
    for product in products:
        product.is_delete = True
        product.save()


@shared_task()
def set_is_active_true_task(product_ids):
    products = Product.objects.filter(id__in=product_ids)
    for product in products:
        product.is_active = True
        product.save()


@shared_task()
def set_is_active_false_task(product_ids):
    products = Product.objects.filter(id__in=product_ids)
    for product in products:
        product.is_active = False
        product.save()


@shared_task()
def set_is_deleted_true_discount_task(product_ids):
    discounts = Discount.objects.filter(id__in=product_ids)
    for discount in discounts:
        discount.is_delete = True
        discount.save()


@shared_task()
def set_is_active_true_discount_task(product_ids):
    discounts = Discount.objects.filter(id__in=product_ids)
    for discount in discounts:
        discount.is_active = True
        discount.save()


@shared_task()
def set_is_active_false_discount_task(product_ids):
    discounts = Discount.objects.filter(id__in=product_ids)
    for discount in discounts:
        discount.is_active = False
        discount.save()
