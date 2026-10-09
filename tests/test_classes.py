"""
Тесты для классов Product и Category.
"""

import pytest

from src.classes import Category, Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self, sample_product):
        """Тест инициализации товара."""
        assert sample_product.name == "Test Product"
        assert sample_product.description == "Test Description"
        assert sample_product.price == 100.0
        assert sample_product.quantity == 10

    def test_product_negative_price_raises_error(self):
        """Тест: цена <= 0 вызывает ошибку ValueError."""
        with pytest.raises(ValueError, match="Цена товара должна быть больше 0"):
            Product("Test", "Description", -100.0, 10)
        with pytest.raises(ValueError, match="Цена товара должна быть больше 0"):
            Product("Test", "Description", 0, 10)

    def test_product_negative_quantity_raises_error(self):
        """Тест: количество < 0 вызывает ошибку ValueError."""
        with pytest.raises(
            ValueError, match="Количество товара не может быть отрицательным"
        ):
            Product("Test", "Description", 100.0, -5)

    def test_product_price_setter_valid(self, sample_product):
        """Тест сеттера цены с валидным значением."""
        sample_product.price = 150.0
        assert sample_product.price == 150.0

    def test_product_price_setter_invalid(self, sample_product, capsys):
        """Тест сеттера цены с невалидным значением (<= 0)."""
        sample_product.price = -50.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert sample_product.price == 100.0

    def test_product_price_setter_zero(self, sample_product, capsys):
        """Тест сеттера цены с нулевым значением."""
        sample_product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert sample_product.price == 100.0

    def test_product_new_product_class_method(self):
        """Тест класс-метода new_product с передачей словаря."""
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

    def test_product_str(self):
        """Тест строкового представления товара."""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."

    @pytest.mark.parametrize("price_a, qty_a, price_b, qty_b, expected", [
        (100.0, 10, 200.0, 2, 1400.0),   # 100*10 + 200*2
        (500.0, 3, 1000.0, 5, 6500.0),   # 500*3 + 1000*5
        (100.0, 0, 200.0, 5, 1000.0),    # 100*0 + 200*5
    ])
    def test_product_add(self, price_a, qty_a, price_b, qty_b, expected):
        """Параметризованный тест магического метода сложения."""
        a = Product("A", "Desc", price_a, qty_a)
        b = Product("B", "Desc", price_b, qty_b)
        assert a + b == expected


class TestCategory:
    """Тесты для класса Category."""

    def test_category_initialization_without_products(self, empty_category):
        """Тест инициализации категории без товаров."""
        assert empty_category.name == "Empty Category"
        assert empty_category._Category__products == []
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_initialization_with_products(self, sample_category):
        """Тест инициализации категории с товарами."""
        assert len(sample_category._Category__products) == 3
        assert Category.category_count == 1
        assert Category.product_count == 3

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

    def test_category_add_product(self):
        """Тест метода add_product."""
        category = Category("Electronics", "All electronics")
        product = Product("New Phone", "Smartphone", 50000.0, 10)
        category.add_product(product)
        assert len(category._Category__products) == 1
        assert Category.product_count == 1

    def test_category_average_price(self, sample_category):
        """Тест расчета средней цены."""
        assert sample_category.average_price() == 200.0

    def test_category_average_price_empty_raises_error(self, empty_category):
        """Тест: пустая категория вызывает ошибку."""
        with pytest.raises(
            ValueError, match="Нет товаров в категории для расчета средней цены"
        ):
            empty_category.average_price()

    def test_category_products_property(self, sample_category):
        """Тест геттера products."""
        expected = (
            "Product 1, 100.0 руб. Остаток: 5 шт.\n"
            "Product 2, 200.0 руб. Остаток: 3 шт.\n"
            "Product 3, 300.0 руб. Остаток: 7 шт."
        )
        assert sample_category.products == expected

    def test_category_products_property_empty(self, empty_category):
        """Тест геттера products для пустой категории."""
        assert empty_category.products == "В категории нет товаров"

    def test_category_private_products_not_accessible(self):
        """Тест: к __products нельзя обратиться напрямую."""
        category = Category("Test", "Desc")
        assert not hasattr(category, "_products")
        assert hasattr(category, "_Category__products")

    def test_category_str(self):
        """Тест строкового представления категории."""
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой", 150000.0, 5)
        category = Category("Электроника", "Все гаджеты", [product1, product2])
        assert str(category) == "Электроника, количество продуктов: 15 шт."

    def test_category_str_empty(self):
        """Тест строкового представления пустой категории."""
        category = Category("Пустая", "Нет товаров")
        assert str(category) == "Пустая, количество продуктов: 0 шт."


class TestIntegration:
    """Интеграционные тесты."""

    def test_full_workflow(self):
        """Полный рабочий процесс."""
        product1 = Product("Phone", "Smartphone", 50000.0, 10)
        product2 = Product("Tablet", "Tablet", 30000.0, 5)
        category = Category("Electronics", "All electronics", [product1])
        category.add_product(product2)
        expected = (
            "Phone, 50000.0 руб. Остаток: 10 шт.\n"
            "Tablet, 30000.0 руб. Остаток: 5 шт."
        )
        assert category.products == expected
        assert category.average_price() == 40000.0
        assert Category.product_count == 2

    def test_new_product_and_add_to_category(self):
        """Тест создания товара через new_product."""
        product_data = {
            'name': 'NewPhone',
            'description': 'Latest model',
            'price': 70000.0,
            'quantity': 20
        }
        product = Product.new_product(product_data)
        category = Category("Smartphones", "All smartphones")
        category.add_product(product)
        assert len(category._Category__products) == 1
        assert category.products == "NewPhone, 70000.0 руб. Остаток: 20 шт."
