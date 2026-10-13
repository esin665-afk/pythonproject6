"""
Тесты для ограничений добавления продуктов в категорию.
"""

import pytest

from src import Category, LawnGrass, Product, Smartphone


def test_add_product_works():
    """Тест: добавление Product работает."""
    cat = Category("Cat", "Desc")
    cat.add_product(Product("A", "D", 100.0, 10))
    assert len(cat._Category__products) == 1


def test_add_smartphone_works():
    """Тест: добавление Smartphone работает (наследник)."""
    cat = Category("Cat", "Desc")
    cat.add_product(Smartphone("iPhone", "D", 100.0, 1, 1.0, "M", 64, "R"))
    assert len(cat._Category__products) == 1


def test_add_lawn_grass_works():
    """Тест: добавление LawnGrass работает (наследник)."""
    cat = Category("Cat", "Desc")
    cat.add_product(LawnGrass("G", "D", 100.0, 1, "RU", "7", "G"))
    assert len(cat._Category__products) == 1


def test_add_string_raises_error():
    """Тест: добавление строки вызывает TypeError."""
    cat = Category("Cat", "Desc")
    with pytest.raises(TypeError):
        cat.add_product("не продукт")


def test_add_number_raises_error():
    """Тест: добавление числа вызывает TypeError."""
    cat = Category("Cat", "Desc")
    with pytest.raises(TypeError):
        cat.add_product(42)


def test_add_none_raises_error():
    """Тест: добавление None вызывает TypeError."""
    cat = Category("Cat", "Desc")
    with pytest.raises(TypeError):
        cat.add_product(None)
