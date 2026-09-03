"""
Тесты для классов Product и Category.
"""

import pytest

from src.main import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сброс счетчиков перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест инициализации товара."""
        product = Product("Test", "Description", 100.0, 10)

        assert product.name == "Test"
        assert product.description == "Description"
        assert product.price == 100.0
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category."""

    def test_category_initialization_without_products(self):
        """Тест инициализации категории без товаров."""
        category = Category("Test Category", "Test Description")

        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert category.products == []
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_initialization_with_products(self):
        """Тест инициализации категории с товарами."""
        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 3)

        category = Category("Test Category", "Test Description", [product1, product2])

        assert len(category.products) == 2
        assert Category.category_count == 1
        assert Category.product_count == 2

    def test_category_count_multiple(self):
        """Тест подсчета нескольких категорий."""
        Category("Category 1", "Description 1")
        Category("Category 2", "Description 2")
        Category("Category 3", "Description 3")

        assert Category.category_count == 3

    def test_product_count_multiple(self):
        """Тест подсчета товаров в нескольких категориях."""
        product1 = Product("Product A", "Description A", 100.0, 1)
        product2 = Product("Product B", "Description B", 200.0, 2)
        product3 = Product("Product C", "Description C", 300.0, 3)

        Category("Category 1", "Description 1", [product1])
        Category("Category 2", "Description 2", [product2, product3])

        assert Category.product_count == 3
