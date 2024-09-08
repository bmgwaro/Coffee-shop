from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")


order1 = Order(customer1, 3.5, coffee1)  
order2 = Order(customer2, 4.0, coffee1)  
order3 = Order(customer3, 5.0, coffee2)  
order4 = Order(customer1, 2.5, coffee1)  

# Test Coffee class methods
print("Orders for Espresso:", coffee1.orders())  # Should show orders associated with Espresso
print("Customers who ordered Espresso:", [customer.name for customer in coffee1.customers()])  # Should list Alice, Bob
print("Number of orders for Espresso:", coffee1.num_orders())  # Should return 3
print("Average price for Espresso:", coffee1.average_price())  # Should return the average price of 3.5, 4.0, and 2.5

print("Orders for Latte:", coffee2.orders())  # Should show orders associated with Latte
print("Customers who ordered Latte:", [customer.name for customer in coffee2.customers()])  # Should list Charlie
print("Number of orders for Latte:", coffee2.num_orders())  # Should return 1
print("Average price for Latte:", coffee2.average_price())  # Should return 5.0