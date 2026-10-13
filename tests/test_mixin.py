"""
Тесты для класса-миксина ReprMixin.
"""

from src import LawnGrass, Product, Smartphone
from src.mixin import ReprMixin


def test_mixin_prints_on_product_creation(capsys):
    """Тест: миксин печатает информацию при создании Product."""
    Product("Тест", "Описание", 100.0, 10)
    captured = capsys.readouterr()
    assert "Product('Тест', 'Описание', 100.0, 10)" in captured.out


def test_mixin_prints_on_smartphone_creation(capsys):
    """Тест: миксин печатает информацию при создании Smartphone."""
    Smartphone("iPhone", "Desc", 100000.0, 5, 3.5, "15", 256, "Black")
    captured = capsys.readouterr()
    assert "Smartphone(" in captured.out
    assert "'iPhone'" in captured.out
    assert "100000.0" in captured.out


def test_mixin_prints_on_lawn_grass_creation(capsys):
    """Тест: миксин печатает информацию при создании LawnGrass."""
    LawnGrass("Газон", "Трава", 500.0, 100, "Россия", "14 дней", "Зеленый")
    captured = capsys.readouterr()
    assert "LawnGrass(" in captured.out
    assert "'Газон'" in captured.out
    assert "500.0" in captured.out


def test_mixin_in_product_mro():
    """Тест: ReprMixin находится в MRO класса Product."""
    assert ReprMixin in Product.__mro__


def test_mixin_in_smartphone_mro():
    """Тест: ReprMixin находится в MRO класса Smartphone."""
    assert ReprMixin in Smartphone.__mro__


def test_mixin_in_lawn_grass_mro():
    """Тест: ReprMixin находится в MRO класса LawnGrass."""
    assert ReprMixin in LawnGrass.__mro__
