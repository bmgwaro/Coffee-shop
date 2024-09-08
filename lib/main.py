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


print("Orders for Espresso:", coffee1.orders())  
print("Customers who ordered Espresso:", [customer.name for customer in coffee1.customers()])  
print("Number of orders for Espresso:", coffee1.num_orders())  
print("Average price for Espresso:", coffee1.average_price())  

print("Orders for Latte:", coffee2.orders())  
print("Customers who ordered Latte:", [customer.name for customer in coffee2.customers()])  
print("Number of orders for Latte:", coffee2.num_orders())  
print("Average price for Latte:", coffee2.average_price())  