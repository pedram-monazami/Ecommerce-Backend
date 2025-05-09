from rest_framework import serializers

from .models import Customer, Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Address model serializer
    """

    class Meta:
        model = Address
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer model serializer
    """

    class Meta:
        model = Customer
        fields = '__all__'
