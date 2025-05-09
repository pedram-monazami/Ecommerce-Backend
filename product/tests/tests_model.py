from django.test import TestCase

from product.models import *


class DiscountTest(TestCase):
    def setUp(self) -> None:
        """
        Testing the creation of the discounts.
        :return:
        """
        self.discount1 = Discount.objects.create(amount=10, description="Christmas", type='cent')
        self.discount2 = Discount.objects.create(amount=20, description="Black Friday", type='val')

    def test_discounted_price(self):
        """
        Testing discounted_price method.
        :return:
        """
        self.assertEqual(self.discount1.discounted_price(100), 90)
        self.assertEqual(self.discount1.discounted_price(200), 180)
        self.assertEqual(self.discount2.discounted_price(100), 80)
        self.assertEqual(self.discount2.discounted_price(200), 180)

    def test_str(self):
        """
        Testing discount str.
        :return:
        """
        self.assertEqual(str('Discount type: cent Amount: 10'), self.discount1.__str__())


class BrandTest(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of brand
        :return:
        """
        self.discount1 = Discount.objects.create(amount=10, description="Christmas", type='cent')
        self.brand1 = Brand.objects.create(name='LG', discount_id=1)
        # self.brand2 = Brand.objects.create(name='Sony')

    def test_str(self):
        """
        Testing brand str
        :return:
        """
        self.assertEqual(str('Brand: LG'), self.brand1.__str__())


class CategoryTest(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of Category
        :return:
        """
        self.discount1 = Discount.objects.create(amount=10, description="Christmas", type='cent')
        self.category1 = Category.objects.create(name='phones', discount_id=1)

    def test_str(self):
        """
        Testing category str
        :return:
        """
        self.assertEqual(str('Category: phones'), self.category1.__str__())


class CommentTest(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of comment
        :return:
        """
        self.comment1 = Comment.objects.create(content='Simple comment')

    def test_str(self):
        """
        Testing comment str
        :return:
        """
        self.assertEqual(str('Comment: Simple comment'), self.comment1.__str__())


class ProductTest(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of product
        :return:
        """
        self.category1 = Category.objects.create(name='phones', discount_id=1)
        self.comment1 = Comment.objects.create(content='Simple comment')
        self.discount1 = Discount.objects.create(amount=10, description="Christmas", type='cent')
        self.brand1 = Brand.objects.create(name='LG', discount_id=1)
        self.product1 = Product.objects.create(name='iphone', description='not a good phone', discount_id=1, brand_id=1,
                                               comment_id=1, price=100, count=5, category_id=1)

    def test_str(self):
        """
        Testing product str
        :return:
        """
        self.assertEqual(str('iphone with price of 100'), self.product1.__str__())
