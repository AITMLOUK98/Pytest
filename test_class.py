import pytest
from main import User, Client, Product, DiscountedProduct


def test_user_greet():
    user = User("John", "john@example.com")
    assert user.greet() == "Hello, John!"


def test_client_get_company_name():
    client = Client("Alice", "alice@example.com", "ABC Inc.")
    assert client.get_company_name() == "Company: ABC Inc."


def test_product_get_info():
    product = Product("Phone", 500)
    assert product.get_info() == "Product: Phone | Price: 500"


def test_discounted_product_get_discounted_price():
    discounted_product = DiscountedProduct("Laptop", 1000, 0.2)
    assert discounted_product.get_discounted_price() == "Discounted Price: 800.0"
