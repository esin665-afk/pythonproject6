"""
Тесты для класса Category.
"""

import pytest

from src.classes import Category, Product


def test_category_initialization_without_products():
    """Тест инициализации категории без товаров."""
    category = Category("Empty Category", "No products")
    assert category.name == "Empty Category"
    assert category._Category__products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_initialization_with_products():
    """Тест инициализации категории с товарами."""
    product1 = Product("P1", "D1", 100.0, 5)
    product2 = Product("P2", "D2", 200.0, 3)
    category = Category("Cat", "Desc", [product1, product2])
    assert len(category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_count_multiple():
    """Тест подсчета нескольких категорий."""
    Category("Cat 1", "D1")
    Category("Cat 2", "D2")
    Category("Cat 3", "D3")
    assert Category.category_count == 3


def test_product_count_multiple():
    """Тест подсчета товаров в нескольких категориях."""
    p1 = Product("A", "D", 100.0, 1)
    p2 = Product("B", "D", 200.0, 2)
    p3 = Product("C", "D", 300.0, 3)
    Category("Cat 1", "D1", [p1])
    Category("Cat 2", "D2", [p2, p3])
    assert Category.product_count == 3


def test_category_add_product():
    """Тест метода add_product."""
    category = Category("Electronics", "All electronics")
    product = Product("New Phone", "Smartphone", 50000.0, 10)
    category.add_product(product)
    assert len(category._Category__products) == 1
    assert Category.product_count == 1


def test_category_average_price():
    """Тест расчета средней цены."""
    p1 = Product("P1", "D1", 100.0, 5)
    p2 = Product("P2", "D2", 200.0, 3)
    p3 = Product("P3", "D3", 300.0, 7)
    category = Category("Cat", "Desc", [p1, p2, p3])
    assert category.average_price() == 200.0


def test_category_average_price_empty_raises_error():
    """Тест: пустая категория вызывает ошибку."""
    category = Category("Empty", "Desc")
    with pytest.raises(ValueError):
        category.average_price()


def test_category_products_property():
    """Тест геттера products."""
    p1 = Product("Product 1", "D1", 100.0, 5)
    p2 = Product("Product 2", "D2", 200.0, 3)
    category = Category("Cat", "Desc", [p1, p2])
    expected = (
        "Product 1, 100.0 руб. Остаток: 5 шт.\n"
        "Product 2, 200.0 руб. Остаток: 3 шт."
    )
    assert category.products == expected


def test_category_products_property_empty():
    """Тест геттера products для пустой категории."""
    category = Category("Empty", "Desc")
    assert category.products == "В категории нет товаров"


def test_category_str():
    """Тест строкового представления категории."""
    p1 = Product("Телефон", "Смартфон", 50000.0, 10)
    p2 = Product("Ноутбук", "Игровой", 150000.0, 5)
    category = Category("Электроника", "Все гаджеты", [p1, p2])
    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_category_str_empty():
    """Тест строкового представления пустой категории."""
    category = Category("Пустая", "Нет товаров")
    assert str(category) == "Пустая, количество продуктов: 0 шт."
