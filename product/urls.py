from django.urls import path

from product.views import *

# The urls of products app.
urlpatterns = [
    path('category', CategoryListView.as_view(), name='category_list'),
    path('category/<str:slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('brand', BrandListView.as_view(), name='brand_list'),
    path('brand/<str:slug>', BrandDetailView.as_view(), name='brand_detail'),
    path('comment', CommentCreateAPIView.as_view(), name='comment_create'),
    path('', ProductListView.as_view(), name='products_list'),
    path('<str:slug>', ProductDetailView.as_view(), name='products_detail'),
]
