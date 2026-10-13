"""
Тесты для класса Product.
"""

import pytest

from src.classes import Product


def test_product_initialization():
    """Тест инициализации товара."""
    product = Product("Test", "Description", 100.0, 10)
    assert product.name == "Test"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_negative_price_raises_error():
    """Тест: цена <= 0 вызывает ошибку ValueError."""
    with pytest.raises(ValueError):
        Product("Test", "Description", -100.0, 10)
    with pytest.raises(ValueError):
        Product("Test", "Description", 0, 10)


def test_product_negative_quantity_raises_error():
    """Тест: количество < 0 вызывает ошибку ValueError."""
    with pytest.raises(ValueError):
        Product("Test", "Description", 100.0, -5)


def test_product_price_setter_valid():
    """Тест сеттера цены с валидным значением."""
    product = Product("Test", "Description", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_invalid(capsys):
    """Тест сеттера цены с невалидным значением."""
    product = Product("Test", "Description", 100.0, 10)
    product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_product_new_product_class_method():
    """Тест класс-метода new_product."""
    product_data = {
        'name': 'NewPhone',
        'description': 'New smartphone',
        'price': 50000.0,
        'quantity': 15
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == 'NewPhone'
    assert product.price == 50000.0


def test_product_str():
    """Тест строкового представления товара."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


@pytest.mark.parametrize("price_a, qty_a, price_b, qty_b, expected", [
    (100.0, 10, 200.0, 2, 1400.0),
    (500.0, 3, 1000.0, 5, 6500.0),
    (100.0, 0, 200.0, 5, 1000.0),
])
def test_product_add(price_a, qty_a, price_b, qty_b, expected):
    """Параметризованный тест магического метода сложения."""
    a = Product("A", "Desc", price_a, qty_a)
    b = Product("B", "Desc", price_b, qty_b)
    assert a + b == expected
