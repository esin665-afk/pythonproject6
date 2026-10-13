"""
Фикстуры для тестов классов.
"""

import pytest

from src.classes import Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    """
    Фикстура для автоматического сброса счетчиков перед каждым тестом.

    Используется autouse=True, чтобы применялась ко всем тестам.
    """
    Category.category_count = 0
    Category.product_count = 0
    yield
