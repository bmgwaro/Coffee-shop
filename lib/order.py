from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, price, coffee):
        if not isinstance(customer, Customer):
            print("customer must be an instance of Customer")
        
        if not isinstance(coffee, Coffee):
            print("coffee must be an instance of Coffee")
        
        if not isinstance(price, float):
            print("price must be a float")
        if not (1.0 <= price <= 10.0):
            print("price must be between 1.0 and 10.0, inclusive")

        self._customer=customer
        self._price=price
        self._coffee=coffee

        coffee.add_order(self)

    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee