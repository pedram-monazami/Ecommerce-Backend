from django.db import IntegrityError
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView, CreateAPIView, \
    RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from core.models import User
from customer.models import Customer, Address
from customer.serializers import AddressSerializer, CustomerSerializer


class AddressListCreateView(ListCreateAPIView):
    """
    A GET/POST api view for filtering and sending addresses of the customer.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Overriding get method for filtering customer addresses.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.queryset.filter(customer__user=self.request.user)
        serialized_data = self.serializer_class(queryset, many=True)

        return Response(serialized_data.data)

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        # request.data._mutable = True
        request.data['customer'] = customer.id
        return super().create(request, *args, **kwargs)


class AddressDestroyView(DestroyAPIView):
    """
    A view for deleting the customer addresses.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]


class ProfileRetrieveUpdateView(RetrieveAPIView):
    """
    A view for showing and updating the customer information.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Overriding this method to show the customer information.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        customer = Customer.objects.get(user=request.user)
        serialized_data = self.serializer_class(customer)
        return Response(serialized_data.data)


class CustomerCreateView(CreateAPIView):
    """
    A view for creating a customer
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(
                email=request.data.get('email'),
                password=request.data.get('password'),
                phone=request.data.get('phone')
            )
        except IntegrityError:
            return HttpResponseBadRequest()
        request.data['user'] = user.id
        return super().post(request, *args, **kwargs)
