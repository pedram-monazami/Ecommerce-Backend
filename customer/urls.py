from django.urls import path

from customer.views import *

# The urls of customer app.
urlpatterns = [
    path('address/', AddressListCreateView.as_view(), name='address_list_create'),
    path('address/<int:pk>', AddressDestroyView.as_view(), name='delete_address'),
    path('register/', CustomerCreateView.as_view(), name='register'),
    path('', ProfileRetrieveUpdateView.as_view(), name='customer_detail_update'),
]

