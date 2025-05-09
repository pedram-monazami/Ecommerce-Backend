from django.test import TestCase

from customer.models import Customer, Address
from product.models import Product, Discount, Brand, Comment, Category
from ..models import Order, OrderItem, Coupon, Status


class TestCoupon(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of Coupon codes
        :return:
        """
        self.coupon1 = Coupon.objects.create(amount=50, type='val', code='new-code', description='new year')
        self.coupon2 = Coupon.objects.create(amount=50, type='cent', code='thanks-code', description='thanksgiving')

    def test_str(self):
        """
        Testing the Coupon str.
        :return:
        """
        self.assertEqual(str('Coupon type:val Amount50 Codenew-code'), self.coupon1.__str__())

    def test_discounted_price(self):
        """
        Testing calculation of coupon code
        :return:
        """
        self.assertEqual(self.coupon1.discounted_price(20), 20)
        self.assertEqual(self.coupon1.discounted_price(200), 150)
        self.assertEqual(self.coupon1.discounted_price(50), 0)
        self.assertEqual(self.coupon2.discounted_price(80), 40)
        self.assertEqual(self.coupon2.discounted_price(200), 100)


class TestStatus(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of Status
        :return:
        """
        self.status1 = Status.objects.create(title="paid")

    def test_str(self):
        """
        Testing status str.
        :return:
        """
        self.assertEqual(str('Status: paid Code: 1'), self.status1.__str__())


class TestOrderItem(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of OrderItem
        :return:
        """
        self.coupon1 = Coupon.objects.create(amount=50, type='val', code='new-code', description='new year')
        self.address1 = Address.objects.create(country='USA', city='Kerman', street='no 59, 56th st',
                                               zipcode='1122334455')
        self.customer1 = Customer.objects.create(name='Mehdi', email='test@test.com', password='123',
                                                 phone="09123456789", address_id=1)
        self.status1 = Status.objects.create(title="paid")
        self.category1 = Category.objects.create(discount_id=1, name='tv')
        self.comment1 = Comment.objects.create(content='Simple comment')
        self.discount1 = Discount.objects.create(amount=10, description="Christmas", type='cent')
        self.brand1 = Brand.objects.create(name='LG', discount_id=1)
        self.product1 = Product.objects.create(name='iphone', description='not a good phone', discount_id=1, brand_id=1,
                                               comment_id=1, price=100, count=5, category_id=1)
        self.order1 = Order.objects.create(total_price=100, final_price=80, coupon_id=1, customer_id=1, status_id=1)
        self.order_item1 = OrderItem.objects.create(product_id=1, order_id=1, count=2)

    def test_str(self):
        self.assertEqual(str('Product: iphone with price of 100 X2'), self.order_item1.__str__())


class TestOrder(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of Order
        :return:
        """
        self.status1 = Status.objects.create(title="paid")
        self.address1 = Address.objects.create(country='USA', city='Kerman', street='no 59, 56th st',
                                               zipcode='1122334455')
        self.customer1 = Customer.objects.create(name='Mehdi', email='test@test.com', password='123',
                                                 phone="09123456789", address_id=1)
        self.coupon1 = Coupon.objects.create(amount=50, type='val', code='new-code', description='new year')
        self.order1 = Order.objects.create(status_id=1, customer_id=1, coupon_id=1, total_price=100, final_price=80)

    def test_str(self):
        """
        Testing order str.
        :return:
        """
        self.assertEqual(str('Order for customer: Name: Mehdi Status: Status: paid Code: 1'), self.order1.__str__())
