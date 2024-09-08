from customer import Customer

class Coffee:
    all_orders=[]
    def __init__(self, name):
        if not isinstance(name, str):
            print("name must be a string")
        
        
        if len(name) < 3:
            print("name must be at least 3 characters long")
        
        
        self._name = name
    
    
    @property
    def name(self):
        return self._name
    
    
    def __setattr__(self, key, value):
        if key == "_name" and hasattr(self, "_name"):
            print("name cannot be changed once set")
        super().__setattr__(key, value)

    def add_order(self, order):
        """Add an order to the all_orders list for this coffee."""
        Coffee.all_orders.append(order)

    def orders(self):
        return [order for order in Coffee.all_orders if order.coffee==self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        coffee_orders = self.orders()
        
        if not coffee_orders:
            return 0
        
        
        total_price = sum(order.price for order in coffee_orders)
        
        
        return total_price / len(coffee_orders)


