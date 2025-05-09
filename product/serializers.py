from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from product.models import *
from core.utils import apply_all_discounts


class CommentSerializer(serializers.ModelSerializer):
    """
    The comment model serializer.
    """

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'product',
            'parent_comment',
            'replies'
        ]
    replies = serializers.SerializerMethodField(read_only=True)

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent_comment=obj.id)
        return CommentReplySerializer(replies, many=True).data


class CommentReplySerializer(serializers.ModelSerializer):
    """
    The comment reply serializer.
    """

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
        ]


class DiscountSerializer(serializers.ModelSerializer):
    """
    The Discount model serializer
    """

    class Meta:
        model = Discount
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    """
    The brand model serializer.
    """

    class Meta:
        model = Brand
        fields = '__all__'

    discount = DiscountSerializer(read_only=True)


class BrandDetailSerializer(serializers.ModelSerializer):
    """
    The brand model serializer with detail.
    """

    class Meta:
        model = Brand
        fields = '__all__'

    discount = DiscountSerializer(read_only=True)
    products = serializers.SerializerMethodField(read_only=True)

    def get_products(self, obj):
        products = Product.objects.filter(brand=obj.id)
        return ProductWithoutBrandSerializer(products, many=True).data


class CategorySerializer(serializers.ModelSerializer):
    """
    The category model serializer.
    """

    class Meta:
        model = Category
        fields = [
            'id',
            'discount',
            'name',
            'parent',
            'children',
            'image',
            'products',
            'slug'
        ]

    children = serializers.SerializerMethodField(read_only=True)
    parent = RecursiveField(allow_null=True)
    discount = DiscountSerializer(read_only=True)
    products = serializers.SerializerMethodField(read_only=True)

    def get_products(self, obj):
        products = Product.objects.filter(category=obj.id)
        return ProductWithoutCategorySerializer(products, many=True).data

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj.id)
        return CategoryWithoutProductsSerializer(children, many=True).data


class CategoryWithoutProductsSerializer(serializers.ModelSerializer):
    """
    The category model serializer.
    """

    class Meta:
        model = Category
        fields = [
            'id',
            'discount',
            'name',
            'parent',
            'image',
            'slug'
        ]

    parent = RecursiveField(allow_null=True)
    discount = DiscountSerializer(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    """
    The product model serializer.
    """

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'brand',
            'image',
            'discount',
            'price',
            'discount_price',
            'count',
            'slug'
        ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }

    brand = BrandSerializer(read_only=True)
    category = CategoryWithoutProductsSerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    discount_price = serializers.SerializerMethodField(read_only=True)

    def get_discount_price(self, obj):
        return apply_all_discounts(obj)


class ProductWithCommentSerializer(serializers.ModelSerializer):
    """
    The product model serializer.
    """

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'brand',
            'image',
            'discount',
            'price',
            'discount_price',
            'count',
            'comments',
            'slug'
        ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }

    comments = serializers.SerializerMethodField(read_only=True)
    brand = BrandSerializer(read_only=True)
    category = CategoryWithoutProductsSerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    discount_price = serializers.SerializerMethodField(read_only=True)

    def get_discount_price(self, obj):
        return apply_all_discounts(obj)

    def get_comments(self, obj):
        comments = Comment.objects.filter(parent_comment=None, product=obj.id)
        return CommentSerializer(comments, many=True).data


class ProductWithoutBrandSerializer(serializers.ModelSerializer):
    """
    The product model serializer without brand field for brand serializer.
    """

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'image',
            'discount',
            'price',
            'discount_price',
            'count',
            'slug'
        ]

    category = CategorySerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    discount_price = serializers.SerializerMethodField(read_only=True)

    def get_discount_price(self, obj):
        return apply_all_discounts(obj)


class ProductWithoutCategorySerializer(serializers.ModelSerializer):
    """
    The product model serializer without category field for category serializer.
    """

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'brand',
            'image',
            'discount',
            'price',
            'discount_price',
            'count',
            'slug'
        ]

    brand = BrandSerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    discount_price = serializers.SerializerMethodField(read_only=True)

    def get_discount_price(self, obj):
        return apply_all_discounts(obj)
