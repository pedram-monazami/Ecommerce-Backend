from rest_framework import serializers

from customer.serializers import CustomerSerializer
from product.serializers import DiscountSerializer, ProductWithoutCategorySerializer
from order.models import Order, OrderItem, Coupon


class OrderSerializer(serializers.ModelSerializer):
    """
    The order model serializer.
    """

    class Meta:
        model = Order
        fields = [
            'id',
            'status',
            'coupon',
            'customer',
            'coupon_details',
            'total_price',
            'final_price',
            'address',
            'order_items',
            'modify_datetime',

        ]
        extra_kwargs = {
            'coupon': {'write_only': True},
            'customer': {'write_only': True},
        }

    coupon_details = DiscountSerializer(read_only=True, source='coupon')
    order_items = serializers.SerializerMethodField(read_only=True)

    def get_order_items(self, obj):
        return OrderItemSerializer(obj.orderitem_set.all(), many=True).data


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    The order model serializer.
    """

    class Meta:
        model = Order
        fields = [
            'id',
            'status',
            'coupon',
            'total_price',
            'final_price',
            'address',
            'order_items',
            'modify_datetime',
        ]

    coupon = DiscountSerializer(read_only=True)
    order_items = serializers.SerializerMethodField(read_only=True)

    def get_order_items(self, obj):
        return OrderItemDetailSerializer(obj.orderitem_set.all(), many=True).data


class OrderItemSerializer(serializers.ModelSerializer):
    """
    The order item model serializer.
    """

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemDetailSerializer(serializers.ModelSerializer):
    """
    The order item model serializer.
    """

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'count',
        ]
    product = ProductWithoutCategorySerializer(read_only=True)


class CouponSerializer(serializers.ModelSerializer):
    """
    The Coupon model serializer.
    """
    class Meta:
        model = Coupon
        fields = '__all__'
