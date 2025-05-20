import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_init(self):
        c = Customer("Tester")
        cf = Coffee("Drip")
        order = Order(c, cf, 5.0)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, cf)
        self.assertEqual(order.price, 5.0)

        with self.assertRaises(TypeError):
            Order("NotCustomer", cf, 5.0)
        with self.assertRaises(ValueError):
            Order(c, cf, 11.0)
