import json

from django.db import models

from customer.models import Customer
from order.models import OrderItem, Order, Coupon
from product.models import Discount, Product


def set_product_cookie(request):
    """
    Reads cookie from request and creates/modifies based on the products.
    :param request:
    :return: Json
    """
    product_id = request.data['product']
    product_count = int(request.data['count'])
    product = request.COOKIES.get('product')
    if product:
        my_dict = json.loads(product)
        if product_id in my_dict.keys():
            my_dict[product_id] = my_dict[product_id] + product_count
            return json.dumps(my_dict)
        my_dict[product_id] = product_count
        return json.dumps(my_dict)
    return json.dumps({product_id: product_count})


def get_cookie(request):
    """
    Reads orders data from cookie and creates an OrderItem models for anonymous user to be shown.
    :param request:
    :return: a list of orders.
    """
    product = request.COOKIES.get('product')
    if product:
        jsoned = json.loads(product)
        order_list = list()
        for product_id, count in jsoned.items():
            order = OrderItem(product_id=int(product_id), count=count)
            order_list.append(order)
        return order_list
    else:
        return 1


def cookie_to_database(request):
    """
    Reads cookie from request and saves OrderItem in database for the current user.
    :param request:
    """
    product = request.COOKIES.get('product')
    jsoned = json.loads(product)
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.get_or_create(customer=customer, status='new')
    for product_id, count in jsoned.items():
        OrderItem.objects.create(order=order[0], product_id=product_id, count=count)


def change_cart_item_count(request, product_id, count):
    """
    Reads cookie data from user request and changes OrderItem count for the current user.
    :param count:
    :param product_id:
    :param request:
    """
    product = request.COOKIES.get('product')
    jsoned = json.loads(product)
    if product_id in jsoned.keys():
        jsoned[product_id] = count
        return json.dumps(jsoned)


def remove_cart_item_count(request, product_id):
    """
    Reads cookie data from user request and removes OrderItem for the current user.
    :param product_id:
    :param request:
    """
    product = request.COOKIES.get('product')
    jsoned = json.loads(product)
    if product_id in jsoned.keys():
        del jsoned[str(product_id)]
        return json.dumps(jsoned)


def apply_all_discounts(product_object) -> int:
    """
    Apply all discounts to product object (category discount, brand discount and product discount).
    :param product_object:
    :return: discounted_price
    """
    discounted_price = product_object.price
    if product_object.discount is not None:
        discounted_price = Discount.discounted_price(product_object.discount, discounted_price)
    if product_object.category.discount is not None:
        discounted_price = Discount.discounted_price(product_object.category.discount, discounted_price)
    if product_object.brand.discount is not None:
        discounted_price = Discount.discounted_price(product_object.brand.discount, discounted_price)
    return discounted_price


def apply_order_total_price(request) -> None:
    order_id = request.data.get('order', None)
    product_id = request.data.get('product', None)
    order = Order.objects.get(id=order_id)
    product = Product.objects.get(id=product_id)
    discounted_price = apply_all_discounts(product)
    try:
        order_item = OrderItem.objects.get(product=product_id, order=order_id)
        total = discounted_price * (request.data.get('count') - order_item.count)
    except models.ObjectDoesNotExist:
        total = discounted_price * request.data.get('count')
    order.total_price += total
    order.save()


def apply_order_final_price(order) -> None:
    if order.coupon:
        order.final_price = Coupon.discounted_price(order.coupon, order.total_price)
    else:
        order.final_price = order.total_price
    order.save()
