from typing import List, Tuple
from products import *
from promotions import *

class Store:
    def __init__(self, products_list: List[Product]):
        # Store active products
        self._products = list(products_list)


    def add_product(self, product: Product):
        """
        Add a product to the store.
        """
        self._products.append(product)


    def remove_product(self, product: Product):
        """
        Remove a product from the store.
        """
        if product in self._products:
            self._products.remove(product)


    def get_total_quantity(self):
        """
        Returns the total quantity of all active products in the store.
        """
        return sum(p.quantity for p in self._products if p.active)


    def get_all_products(self):
        """
        Returns a list of all active products in the store.
        """
        return [p for p in self._products if p.active]


    def order(self, shopping_list: List[Tuple[Product, int]]):
        """
        Processes an order given a list of (Product, quantity) tuples.
        Reduces the stock and returns the total price.
        """
        total_price = 0.0
        for prod_obj, qty in shopping_list:
            store_prod = next((p for p in self._products if p.name == prod_obj.name), None)
            # deduct and accumulate
            try:
                total_price += store_prod.buy(qty)
            except Exception as e:
                print(e)
        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, order_max=1)
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].promotion = second_half_price
    product_list[1].promotion = third_one_free
    product_list[3].promotion = thirty_percent

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(f"default {best_buy.order([(products[0], 1), (products[1], 2)])}")
    print(f"second_half_price {best_buy.order([(products[0], 4)])}")
    print(f"third_one_free {best_buy.order([(products[1], 4)])}")
    print(f"thirty_percent {best_buy.order([(products[3], 4)])}")


if __name__ == "__main__":
    main()
