class Product:
    """
    A class representing a product in a store.
    """

    def __init__(self, name, price, quantity, promotion=None):
        """
        Initializes a product with a name, price, quantity, and optional promotion.

        Args:
            name (str): The name of the product.
            price (float): The price per unit.
            quantity (int): The amount of product in stock.
            promotion (Promotion, optional): An optional promotion to apply when buying.

        Raises:
            ValueError: If name is empty, or price/quantity are negative.
        """
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
        self._promotion = promotion

    def get_quantity(self):
        """
        Returns the available quantity of the product.

        Returns:
            int: The current quantity.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The new quantity.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("quantity must not be negative")
        self.quantity = quantity

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    @property
    def promotion(self):
        """
        Gets the promotion assigned to the product.

        Returns:
            Promotion: The current promotion.
        """
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        """
        Sets a promotion for the product.

        Args:
            value (Promotion): The promotion to assign.
        """
        self._promotion = value

    def show(self):
        """
        Displays product details including promotion if applicable.

        Returns:
            str: A string representation of the product.
        """
        text = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        promotion_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return text + promotion_text

    def buy(self, quantity):
        """
        Processes a purchase of the product, applying promotions if available.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: Total price after any discounts.

        Raises:
            ValueError: If quantity is invalid or exceeds available stock.
        """
        if quantity < 0:
            raise ValueError("quantity must not be negative")
        if type(self) != NonStockedProduct and quantity > self.quantity:
            raise ValueError("the quantity to buy is more than what is in stock")

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        discount = self.promotion.apply_promotion(self, quantity) if self.promotion else 0
        return quantity * self.price - discount


class NonStockedProduct(Product):
    """
    Represents a product that is always in stock (non-stocked, like digital goods).
    """

    def __init__(self, name, price):
        """
        Initializes a non-stocked product with unlimited quantity.

        Args:
            name (str): Product name.
            price (float): Product price.
        """
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        """Overrides set_quantity to always be 0 for non-stocked products."""
        self.quantity = 0

    def show(self):
        """
        Displays product details for a non-stocked product.

        Returns:
            str: A string representation.
        """
        text = f"{self.name}, Price: {self.price}, Quantity: Unlimited"
        promotion_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return text + promotion_text

    def buy(self, quantity):
        """
        Processes a purchase for a non-stocked product.

        Args:
            quantity (int): Quantity to 'buy'.

        Returns:
            float: Total price after discounts.
        """
        result = super().buy(quantity)
        self.active = True
        self.quantity = 0
        return result


class LimitedProduct(Product):
    """
    Represents a product with a purchase limit per order.
    """

    def __init__(self, name, quantity, price, order_max):
        """
        Initializes a limited product with a purchase cap.

        Args:
            name (str): Product name.
            quantity (int): Available quantity.
            price (float): Price per unit.
            order_max (int): Maximum units allowed per purchase.
        """
        super().__init__(name, price, quantity)
        self.order_max = order_max

    def show(self):
        """
        Displays product details for a limited product.

        Returns:
            str: A string representation.
        """
        text = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Limited to {self.order_max} per order!"
        promotion_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return text + promotion_text

    def buy(self, quantity):
        """
        Processes a purchase and enforces purchase limit.

        Args:
            quantity (int): Quantity to buy.

        Returns:
            float: Total price after discounts.

        Raises:
            ValueError: If quantity exceeds order_max.
        """
        if quantity > self.order_max:
            raise ValueError(f"Can only buy {self.order_max}")
        return super().buy(quantity)


def main():
    """
    Test/demo usage of the Product class and its subclasses.
    """
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
