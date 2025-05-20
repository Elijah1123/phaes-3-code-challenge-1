import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("a" * 16)
        c = Customer("Valid")
        self.assertEqual(c.name, "Valid")

    def test_orders_and_coffees(self):
        c = Customer("Test")
        cf = Coffee("Mocha")
        c.create_order(cf, 3.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertIn(cf, c.coffees())