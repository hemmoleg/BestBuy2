from abc import ABC, abstractmethod

class Promotion(ABC):

    def __init__(self, name):
        self.name = name


    def name(self):
        return self.name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        if quantity >= 2:
            return product.price * (0.5)

        return 0


class ThirdOneFree(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity >= 3:
            return product.price

        return 0


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        return product.price * quantity * (self.percent / 100)