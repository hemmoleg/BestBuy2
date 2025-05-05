from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store
from products import Product, NonStockedProduct, LimitedProduct

# Initialize product catalog with various product types
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, order_max=1)
]

# Create promotion catalog
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

# Assign promotions to specific products
product_list[0].promotion = second_half_price
product_list[1].promotion = third_one_free
product_list[3].promotion = thirty_percent

# Instantiate the store with the product list
STORE = Store(product_list)


def make_order_item(products):
    """
    Prompts the user to select a product and quantity from the product list.

    Args:
        products (list): List of Product instances available in the store.

    Returns:
        tuple: A tuple of (Product, int) representing the selected product and quantity.
        bool: False if the user input is empty or invalid.
    """
    index = 1
    print("---")
    for p in products:
        print(f"{index}. {p.show()}")
        index += 1
    print("---")
    print("When you want to finish order, enter empty text.")
    p_choice = input("Which product number do you want? ")
    am_choice = input("What amount do you want? ")

    if not am_choice:
        return False

    if int(p_choice) < 1 or int(p_choice) > len(products):
        print("Error adding product!")
        return False

    return products[int(p_choice) - 1], int(am_choice)


def make_order(store):
    """
    Collects multiple order items from the user and processes the total order.

    Args:
        store (Store): The store instance to order from.
    """
    order_items = []
    while True:
        order_item = make_order_item(store.get_all_products())
        if order_item:
            order_items.append(order_item)
            print("Product added to list!")
            print("")
        else:
            break

    if len(order_items) > 0:
        print()
        print("*********")
        total_price = store.order(order_items)
        if total_price:
            print(f"Order made! Total Payment: {total_price}")
        else:
            return


def start(store):
    """
    Starts the main user interface for interacting with the store via terminal.

    Args:
        store (Store): The store instance being managed.
    """
    best_buy = store

    while True:
        print("   Store")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = int(input("Please choose a number "))

        if choice == 1:
            for p in best_buy.get_all_products():
                print(p.show())
            print()
        elif choice == 2:
            print(f"Total of {best_buy.get_total_quantity()} items in store")
            print()
        elif choice == 3:
            make_order(best_buy)
            print()
        elif choice == 4:
            exit()


if __name__ == '__main__':
    start(STORE)
