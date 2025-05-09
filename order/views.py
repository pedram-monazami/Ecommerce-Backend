import logging
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.response import Response
from core.utils import apply_all_discounts, apply_order_total_price, apply_order_final_price, set_product_cookie
# from core.utils import set_product_cookie, get_cookie, change_cart_item_count, remove_cart_item_count
from customer.models import Customer
from order.serilizers import OrderSerializer, CouponSerializer, OrderDetailSerializer
from .models import OrderItem, Order, Coupon
from .serilizers import OrderItemSerializer


class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieve, update and destroy order
    """
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponse('anonymous user', status=200)

    def patch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            obj = self.get_object()
            customer = Customer.objects.get(user=request.user)
            if obj.customer_id == customer.id:
                return super().partial_update(request, *args, **kwargs)
            return HttpResponse(
                "Unauthorized. The order you want to  change isn't belong to this customer",
                status=401
            )
        else:
            return HttpResponse('anonymous user', status=200)

    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            obj = self.get_object()
            customer = Customer.objects.get(user=request.user)
            if obj.customer_id == customer.id:
                return super().destroy(request, *args, **kwargs)
            return HttpResponse(
                "Unauthorized. The order you want to  delete isn't belong to this customer",
                status=401
            )
        else:
            return HttpResponse('anonymous user', status=200)


class OrderListCreateView(generics.ListCreateAPIView):
    """
    A view for list and create order
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.get(user=request.user)
            customer_orders = Order.objects.filter(customer=customer)
            serialized_data = self.serializer_class(customer_orders, many=True)
            return Response(serialized_data.data)
        else:
            return HttpResponse('anonymous user', status=200)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.get(user=request.user)
            # request.data._mutable = True
            request.data['customer'] = customer.id
            return super().create(request, *args, **kwargs)
        else:
            return HttpResponse('anonymous user', status=200)


class OrderItemView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    """
    A multipurpose view for OrderItem objects
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            apply_order_total_price(request)
            order = Order.objects.get(id=request.data.get('order'))
            apply_order_final_price(order)
            return super().create(request, *args, **kwargs)
        else:
            return HttpResponse('anonymous user', status=200)

    def partial_update(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            apply_order_total_price(request)
            order = Order.objects.get(id=request.data.get('order'))
            apply_order_final_price(order)
            return super().partial_update(request, *args, **kwargs)
        else:
            return HttpResponse('anonymous user', status=200)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            orderitem = self.get_object()
            order = orderitem.order
            order.total_price -= apply_all_discounts(orderitem.product) * orderitem.count
            order.save()
            apply_order_final_price(order)
            return super().destroy(request, *args, **kwargs)
        else:
            return HttpResponse('anonymous user', status=200)


class CouponView(generics.RetrieveAPIView):
    """
    A view for getting coupon objects
    """
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()


class CouponImplantView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for validating coupon code
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def partial_update(self, request, *args, **kwargs):
        """
        Updating order for the current user if the code is valid
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        order = self.get_object()
        if order.coupon is None:
            try:
                coupon = Coupon.objects.get(code=request.data['coupon'])
                order.coupon = coupon
                order.save()
                apply_order_final_price(order)
                return Response(status=200)
            except Exception as e:
                logging.error(e)
                return Response('No such code', status=400)
        return Response('A code already applied', status=400)
