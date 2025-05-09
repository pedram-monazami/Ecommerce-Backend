from django.urls import path
from order.views import *

# The urls of orders app
urlpatterns = [
    path('', OrderListCreateView.as_view(), name='orders_list_create'),
    path('<int:pk>', OrderRUDView.as_view(), name='orders_RUD'),
    path('coupon/<int:pk>', CouponView.as_view(), name='coupon_get'),
    path('order_coupon/<int:pk>', CouponImplantView.as_view(), name='coupon'),
    path('orderitem/', OrderItemView.as_view(), name='orderitem_create'),
    path('orderitem/<int:pk>', OrderItemView.as_view(), name='orderitem_delete_update'),
]
