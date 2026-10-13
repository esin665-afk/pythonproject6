"""
Тесты для класса LawnGrass.
"""

import pytest

from src import LawnGrass, Product, Smartphone


def test_lawn_grass_initialization():
    """Тест инициализации газонной травы."""
    grass = LawnGrass(
        "Газон", "Трава", 500.0, 100,
        "Россия", "14 дней", "Зеленый"
    )
    assert grass.name == "Газон"
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зеленый"


def test_lawn_grass_is_product_subclass():
    """Тест: LawnGrass является наследником Product."""
    assert issubclass(LawnGrass, Product)


def test_add_same_class_lawn_grass():
    """Тест: сложение двух LawnGrass работает."""
    g1 = LawnGrass("G1", "D", 500.0, 100, "RU", "14 дней", "Green")
    g2 = LawnGrass("G2", "D", 300.0, 50, "RU", "10 дней", "Dark")
    assert g1 + g2 == 65000.0


def test_add_smartphone_and_lawn_grass_raises_error():
    """Тест: сложение Smartphone и LawnGrass вызывает TypeError."""
    s = Smartphone("iPhone", "D", 100000.0, 5, 3.5, "15", 256, "Black")
    g = LawnGrass("G", "D", 500.0, 100, "RU", "14 дней", "Green")
    with pytest.raises(TypeError):
        s + g
