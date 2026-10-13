"""
Тесты для абстрактного класса BaseProduct.
"""

import pytest

from src.base_product import BaseProduct
from src import LawnGrass, Product, Smartphone


def test_base_product_is_abstract():
    """Тест: BaseProduct — абстрактный класс, нельзя создать экземпляр."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 10)


def test_base_product_has_abstract_methods():
    """Тест: BaseProduct имеет абстрактные методы."""
    assert "__str__" in BaseProduct.__abstractmethods__
    assert "__add__" in BaseProduct.__abstractmethods__


def test_product_is_subclass_of_base_product():
    """Тест: Product является наследником BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_smartphone_is_subclass_of_base_product():
    """Тест: Smartphone наследуется от BaseProduct через Product."""
    assert issubclass(Smartphone, BaseProduct)


def test_lawn_grass_is_subclass_of_base_product():
    """Тест: LawnGrass наследуется от BaseProduct через Product."""
    assert issubclass(LawnGrass, BaseProduct)
