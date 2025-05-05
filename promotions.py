from abc import ABC, abstractmethod

class Promotion(ABC):
    """
    Abstract base class for all types of promotions.
    """

    def __init__(self, name):
        """
        Initializes the promotion with a name.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    def name(self):
        """
        Returns the name of the promotion.

        Returns:
            str: The promotion name.
        """
        return self.name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Applies the promotion logic to the given product and quantity.

        Args:
            product (Product): The product being purchased.
            quantity (int): The quantity of the product.

        Returns:
            float: The discount amount to be applied.
        """
        pass


class SecondHalfPrice(Promotion):
    """
    Promotion that gives a 50% discount on the second item if at least 2 items are bought.
    """

    def __init__(self, name):
        """
        Initializes the SecondHalfPrice promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Applies the second half price promotion.

        Args:
            product (Product): The product being purchased.
            quantity (int): The quantity of the product.

        Returns:
            float: The discount amount.
        """
        if quantity >= 2:
            return product.price * 0.5
        return 0


class ThirdOneFree(Promotion):
    """
    Promotion that gives every third item for free.
    """

    def __init__(self, name):
        """
        Initializes the ThirdOneFree promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Applies the third one free promotion.

        Args:
            product (Product): The product being purchased.
            quantity (int): The quantity of the product.

        Returns:
            float: The discount amount.
        """
        if quantity >= 3:
            return product.price  # One item free
        return 0


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage-based discount.
    """

    def __init__(self, name, percent):
        """
        Initializes the PercentDiscount promotion.

        Args:
            name (str): The name of the promotion.
            percent (float): The discount percentage.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Applies a percentage discount based on total quantity.

        Args:
            product (Product): The product being purchased.
            quantity (int): The quantity of the product.

        Returns:
            float: The discount amount.
        """
        return product.price * quantity * (self.percent / 100)
