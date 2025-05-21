import pytest
from products import Product


def test_create_product():
    p = Product("testName", 300, 10)

    assert isinstance(p, Product)

    assert p.name == "testName"
    assert p.price == 300
    assert p.quantity == 10

def test_invalid_create_product():
    with pytest.raises(ValueError):
        p = Product("testName", -10, 30)
        p = Product("", 10, 30)

def test_set_inactive():
    p = Product("testName", 30, 10)
    assert p.buy(10) == 300
    assert p.is_active() is False

def test_too_large_quantity():
    with pytest.raises(ValueError):
        p = Product("testName", 10, 30)
        p.buy(50)

def test_product_purchase():
    p = Product("testName", 30, 10)
    cost = p.buy(7)
    assert cost == 210
    assert p.quantity == 3

pytest.main()