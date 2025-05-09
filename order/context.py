import json

from order.models import Order, OrderItem


def cart_number(request):
    """
    A context manager for the number in navbar shopping cart
    :param request:
    :return: A number to be place in navbar
    """
    if request.user.is_authenticated:
        try:
            order = Order.objects.filter(customer__user=request.user, status='new')[0]
        except:
            return {'number': 0}
        order_item = OrderItem.objects.filter(order=order)
        number = 0
        for item in order_item:
            number += item.count
        return {'number': number}
    else:
        # if user is not authenticated.
        cookie = request.COOKIES.get('product')
        try:
            number = 0
            jsoned = json.loads(cookie)
            for item in jsoned.values():
                number += item
            return {'number': number}
        except:
            return {'number': 0}
