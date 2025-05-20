import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("a")
        c = Coffee("Americano")
        self.assertEqual(c.name, "Americano")

    def test_aggregates(self):
        c1 = Customer("User1")
        c2 = Customer("User2")
        cf = Coffee("Flat White")
        c1.create_order(cf, 2.5)
        c2.create_order(cf, 3.5)
        self.assertEqual(cf.num_orders(), 2)
        self.assertAlmostEqual(cf.average_price(), 3.0)
