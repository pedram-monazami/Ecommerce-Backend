from django.test import TestCase

from ..models import Customer, Address


class CustomerTest(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of Customers
        :return:
        """
        self.address1 = Address.objects.create(country='USA', city='Kerman', street='no 59, 56th st',
                                               zipcode='1122334455')
        self.customer1 = Customer.objects.create(name='Mehdi', email='test@test.com', password='123',
                                                 phone="09123456789", address_id=1)

    def test_fields(self):
        """
        Testing customer fields
        :return:
        """
        self.assertEqual(str('Mehdi'), self.customer1.name)
        self.assertEqual(str('test@test.com'), self.customer1.email)
        self.assertEqual(str('123'), self.customer1.password)
        self.assertEqual(str('09123456789'), self.customer1.phone)

    def test_str(self):
        """
        Testing customer str
        :return:
        """
        self.assertEqual(str('Name: Mehdi'), self.customer1.__str__())


class AddressTest(TestCase):
    def setUp(self) -> None:
        """
        Testing creation of Address
        :return:
        """
        self.address1 = Address.objects.create(country='USA', city='Kerman', street='no 59, 56th st',
                                               zipcode='1122334455')

    def test_fields(self):
        """
        Testing address fields
        :return:
        """
        self.assertEqual(str('USA'), self.address1.country)
        self.assertEqual(str('Kerman'), self.address1.city)
        self.assertEqual(str('no 59, 56th st'), self.address1.street)
        self.assertEqual(str('1122334455'), self.address1.zipcode)

    def test_str(self):
        """
        Testing address str
        :return:
        """
        self.assertEqual(str('Address: no 59, 56th st , Kerman , USA Postal Code: 1122334455'), self.address1.__str__())
