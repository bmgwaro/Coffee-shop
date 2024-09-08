class Customer:
    all_orders=[]
    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name=name.title()
        self.name=name

    @property
    def customer_name(self):
        return self._name

    @customer_name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name=new_name.title()
        else:
            print("Names must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Customer.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))



    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            print("coffee must be an instance of Coffee")
        if not isinstance(price, (int, float)):
            print("price must be a number")
        if not (1.0 <= price <= 10.0):
            print("price must be between 1.0 and 10.0")

        
        new_order = Order(self, coffee, price)
        Customer.all_orders.append(new_order)
        return new_order
