"""
Фикстуры для тестов классов Product и Category.
"""

import pytest

from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """
    Фикстура для автоматического сброса счетчиков перед каждым тестом.

    Используется autouse=True, чтобы применялась ко всем тестам.
    """
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def sample_product():
    """
    Фикстура для создания одного тестового товара.

    Returns:
        Product: Экземпляр товара
    """
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_products():
    """
    Фикстура для создания списка тестовых товаров.

    Returns:
        List[Product]: Список из трех товаров
    """
    return [
        Product("Product 1", "Description 1", 100.0, 5),
        Product("Product 2", "Description 2", 200.0, 3),
        Product("Product 3", "Description 3", 300.0, 7),
    ]


@pytest.fixture
def sample_category(sample_products):
    """
    Фикстура для создания категории с товарами.

    Args:
        sample_products: Фикстура со списком товаров

    Returns:
        Category: Экземпляр категории
    """
    return Category("Test Category", "Test Description", sample_products)


@pytest.fixture
def empty_category():
    """
    Фикстура для создания пустой категории.

    Returns:
        Category: Экземпляр категории без товаров
    """
    return Category("Empty Category", "No products")
