class Product:

    def __init__(self, name, price, quantity):
       self.active = True

       if not name:
           raise ValueError("name must not be empty")
       if price < 0:
           raise ValueError("price must not be negative")
       if quantity < 0:
           raise ValueError("quantity must not be negative")

       self.name = name
       self.price = price
       self.quantity = quantity


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("quantity must not be negative")
        self.quantity = quantity


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        if quantity < 0:
            raise ValueError("quantity must not be negative")
        if quantity > self.quantity:
            raise ValueError("the quantity to buy is more than what is in stock")

        self.quantity -= quantity
        return quantity * self.price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())
    print(bose.name)

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == '__main__':
    main()