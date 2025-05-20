from customer import Customer
from coffee import Coffee
from order import Order

# Example Usage
c1 = Customer("Alice")
c2 = Customer("Bob")
cf1 = Coffee("Latte")
cf2 = Coffee("Espresso")

c1.create_order(cf1, 3.5)
c1.create_order(cf2, 4.0)
c2.create_order(cf1, 5.0)

print(cf1.customers())  # Should show [Alice, Bob]
print(cf1.num_orders())  # Should be 2
print(cf1.average_price())  # Should be 4.25
print(Customer.most_aficionado(cf1))  # Should be Alice