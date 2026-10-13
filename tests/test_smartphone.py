"""
Тесты для класса Smartphone.
"""

import pytest

from src.product import Product
from src.smartphone import Smartphone


def test_smartphone_initialization():
    """Тест инициализации смартфона."""
    phone = Smartphone(
        "iPhone 15", "Флагман", 100000.0, 5,
        3.5, "15 Pro", 256, "Black"
    )
    assert phone.name == "iPhone 15"
    assert phone.efficiency == 3.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Black"


def test_smartphone_is_product_subclass():
    """Тест: Smartphone является наследником Product."""
    assert issubclass(Smartphone, Product)


def test_add_same_class_smartphones():
    """Тест: сложение двух Smartphone работает."""
    s1 = Smartphone("iPhone", "D", 100000.0, 5, 3.5, "15", 256, "Black")
    s2 = Smartphone("Samsung", "D", 80000.0, 3, 3.0, "S23", 128, "White")
    assert s1 + s2 == 740000.0


def test_add_different_classes_raises_error():
    """Тест: сложение Product и Smartphone вызывает TypeError."""
    p = Product("A", "D", 100.0, 10)
    s = Smartphone("iPhone", "D", 100000.0, 5, 3.5, "15", 256, "Black")
    with pytest.raises(TypeError):
        p + s
