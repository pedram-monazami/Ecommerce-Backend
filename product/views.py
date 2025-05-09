from django.http import HttpResponseBadRequest
from rest_framework import generics
from rest_framework.permissions import AllowAny

from product.models import Product, Category, Brand, Comment
from product.serializers import ProductSerializer, CategorySerializer, BrandSerializer, BrandDetailSerializer, \
    ProductWithCommentSerializer, CommentSerializer


class ProductListView(generics.ListAPIView):
    """
    A view to filter and show the products.
    """
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        categories = self.request.query_params.getlist('category')
        brands = self.request.query_params.getlist('brand')
        name = self.request.query_params.get('name', None)
        min_price = self.request.query_params.get('from')
        max_price = self.request.query_params.get('to')
        queryset = Product.objects.all()
        if len(categories) != 0:
            queryset = queryset.filter(category__name__in=categories)

        if len(brands) != 0:
            queryset = queryset.filter(brand__name__in=brands)

        if name is not None:
            queryset = queryset.filter(name__contains=name)

        try:
            if min_price is not None:
                queryset = queryset.filter(price__gte=int(min_price))

            if max_price is not None:
                queryset = queryset.filter(price__lte=int(max_price))

        except TypeError:
            return HttpResponseBadRequest("Invalid value for 'from' or 'to' parameter")

        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    """
    A view to show single product
    """
    serializer_class = ProductWithCommentSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class CategoryListView(generics.ListAPIView):
    """
    A view to list the categories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]


class CategoryDetailView(generics.RetrieveAPIView):
    """
    A view to show single category
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class BrandListView(generics.ListAPIView):
    """
    A view to list the brands
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [AllowAny]


class BrandDetailView(generics.RetrieveAPIView):
    """
    A view to show single brand
    """
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class CommentCreateAPIView(generics.CreateAPIView):
    """
    A view to create a comment
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
