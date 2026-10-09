"""
Тесты для классов Product, Category, Smartphone и LawnGrass.
"""

import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


# ============ ТЕСТЫ ДЛЯ PRODUCT ============

def test_product_initialization():
    """Тест инициализации товара."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_negative_price_raises_error():
    """Тест: цена <= 0 вызывает ошибку ValueError."""
    with pytest.raises(ValueError):
        Product("Test", "Description", -100.0, 10)
    with pytest.raises(ValueError):
        Product("Test", "Description", 0, 10)


def test_product_negative_quantity_raises_error():
    """Тест: количество < 0 вызывает ошибку ValueError."""
    with pytest.raises(ValueError):
        Product("Test", "Description", 100.0, -5)


def test_product_price_setter_valid():
    """Тест сеттера цены с валидным значением."""
    product = Product("Test", "Description", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_invalid(capsys):
    """Тест сеттера цены с невалидным значением."""
    product = Product("Test", "Description", 100.0, 10)
    product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_product_price_setter_zero(capsys):
    """Тест сеттера цены с нулевым значением."""
    product = Product("Test", "Description", 100.0, 10)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_product_new_product_class_method():
    """Тест класс-метода new_product."""
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


def test_product_str():
    """Тест строкового представления товара."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


@pytest.mark.parametrize("price_a, qty_a, price_b, qty_b, expected", [
    (100.0, 10, 200.0, 2, 1400.0),
    (500.0, 3, 1000.0, 5, 6500.0),
    (100.0, 0, 200.0, 5, 1000.0),
])
def test_product_add(price_a, qty_a, price_b, qty_b, expected):
    """Параметризованный тест магического метода сложения."""
    a = Product("A", "Desc", price_a, qty_a)
    b = Product("B", "Desc", price_b, qty_b)
    assert a + b == expected


# ============ ТЕСТЫ ДЛЯ CATEGORY ============

def test_category_initialization_without_products():
    """Тест инициализации категории без товаров."""
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Empty Category", "No products")
    assert category.name == "Empty Category"
    assert category._Category__products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_initialization_with_products():
    """Тест инициализации категории с товарами."""
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("P1", "D1", 100.0, 5)
    product2 = Product("P2", "D2", 200.0, 3)
    category = Category("Cat", "Desc", [product1, product2])
    assert len(category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_count_multiple():
    """Тест подсчета нескольких категорий."""
    Category.category_count = 0
    Category.product_count = 0
    Category("Category 1", "Description 1")
    Category("Category 2", "Description 2")
    Category("Category 3", "Description 3")
    assert Category.category_count == 3


def test_product_count_multiple():
    """Тест подсчета товаров в нескольких категориях."""
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("A", "D", 100.0, 1)
    product2 = Product("B", "D", 200.0, 2)
    product3 = Product("C", "D", 300.0, 3)
    Category("Cat 1", "D1", [product1])
    Category("Cat 2", "D2", [product2, product3])
    assert Category.product_count == 3


def test_category_add_product():
    """Тест метода add_product."""
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Electronics", "All electronics")
    product = Product("New Phone", "Smartphone", 50000.0, 10)
    category.add_product(product)
    assert len(category._Category__products) == 1
    assert Category.product_count == 1


def test_category_average_price():
    """Тест расчета средней цены."""
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("P1", "D1", 100.0, 5)
    product2 = Product("P2", "D2", 200.0, 3)
    product3 = Product("P3", "D3", 300.0, 7)
    category = Category("Cat", "Desc", [product1, product2, product3])
    assert category.average_price() == 200.0


def test_category_average_price_empty_raises_error():
    """Тест: пустая категория вызывает ошибку."""
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Empty", "Desc")
    with pytest.raises(ValueError):
        category.average_price()


def test_category_products_property():
    """Тест геттера products."""
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("Product 1", "D1", 100.0, 5)
    product2 = Product("Product 2", "D2", 200.0, 3)
    category = Category("Cat", "Desc", [product1, product2])
    expected = (
        "Product 1, 100.0 руб. Остаток: 5 шт.\n"
        "Product 2, 200.0 руб. Остаток: 3 шт."
    )
    assert category.products == expected


def test_category_products_property_empty():
    """Тест геттера products для пустой категории."""
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Empty", "Desc")
    assert category.products == "В категории нет товаров"


def test_category_private_products_not_accessible():
    """Тест: к __products нельзя обратиться напрямую."""
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Test", "Desc")
    assert not hasattr(category, "_products")
    assert hasattr(category, "_Category__products")


def test_category_str():
    """Тест строкового представления категории."""
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 150000.0, 5)
    category = Category("Электроника", "Все гаджеты", [product1, product2])
    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_category_str_empty():
    """Тест строкового представления пустой категории."""
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Пустая", "Нет товаров")
    assert str(category) == "Пустая, количество продуктов: 0 шт."


# ============ ТЕСТЫ ДЛЯ SMARTPHONE ============

def test_smartphone_initialization():
    """Тест инициализации смартфона."""
    phone = Smartphone(
        "iPhone 15", "Флагман", 100000.0, 5,
        3.5, "15 Pro", 256, "Black"
    )
    assert phone.name == "iPhone 15"
    assert phone.price == 100000.0
    assert phone.quantity == 5
    assert phone.efficiency == 3.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Black"


def test_smartphone_is_product_subclass():
    """Тест: Smartphone является наследником Product."""
    assert issubclass(Smartphone, Product)
    phone = Smartphone("Test", "Desc", 100.0, 1, 1.0, "M", 64, "Red")
    assert isinstance(phone, Product)


# ============ ТЕСТЫ ДЛЯ LAWINGRASS ============

def test_lawn_grass_initialization():
    """Тест инициализации газонной травы."""
    grass = LawnGrass(
        "Газон", "Трава", 500.0, 100,
        "Россия", "14 дней", "Зеленый"
    )
    assert grass.name == "Газон"
    assert grass.price == 500.0
    assert grass.quantity == 100
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зеленый"


def test_lawn_grass_is_product_subclass():
    """Тест: LawnGrass является наследником Product."""
    assert issubclass(LawnGrass, Product)
    grass = LawnGrass("Test", "Desc", 100.0, 1, "RU", "7 дней", "Green")
    assert isinstance(grass, Product)


# ============ ТЕСТЫ ДЛЯ ОГРАНИЧЕНИЙ СЛОЖЕНИЯ ============

def test_add_same_class_smartphones():
    """Тест: сложение двух Smartphone работает."""
    s1 = Smartphone("iPhone", "D", 100000.0, 5, 3.5, "15", 256, "Black")
    s2 = Smartphone("Samsung", "D", 80000.0, 3, 3.0, "S23", 128, "White")
    assert s1 + s2 == 740000.0


def test_add_same_class_lawn_grass():
    """Тест: сложение двух LawnGrass работает."""
    g1 = LawnGrass("G1", "D", 500.0, 100, "RU", "14 дней", "Green")
    g2 = LawnGrass("G2", "D", 300.0, 50, "RU", "10 дней", "Dark")
    assert g1 + g2 == 65000.0


def test_add_different_classes_raises_error():
    """Тест: сложение Product и Smartphone вызывает TypeError."""
    p = Product("A", "D", 100.0, 10)
    s = Smartphone("iPhone", "D", 100000.0, 5, 3.5, "15", 256, "Black")
    with pytest.raises(TypeError):
        p + s


def test_add_smartphone_and_lawn_grass_raises_error():
    """Тест: сложение Smartphone и LawnGrass вызывает TypeError."""
    s = Smartphone("iPhone", "D", 100000.0, 5, 3.5, "15", 256, "Black")
    g = LawnGrass("G", "D", 500.0, 100, "RU", "14 дней", "Green")
    with pytest.raises(TypeError):
        s + g


# ============ ТЕСТЫ ДЛЯ ОГРАНИЧЕНИЙ ДОБАВЛЕНИЯ ============

def test_add_smartphone_to_category():
    """Тест: добавление Smartphone работает."""
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Cat", "Desc")
    cat.add_product(Smartphone("iPhone", "D", 100.0, 1, 1.0, "M", 64, "R"))
    assert len(cat._Category__products) == 1


def test_add_lawn_grass_to_category():
    """Тест: добавление LawnGrass работает."""
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Cat", "Desc")
    cat.add_product(LawnGrass("G", "D", 100.0, 1, "RU", "7", "G"))
    assert len(cat._Category__products) == 1


def test_add_string_raises_error():
    """Тест: добавление строки вызывает TypeError."""
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Cat", "Desc")
    with pytest.raises(TypeError):
        cat.add_product("не продукт")


def test_add_number_raises_error():
    """Тест: добавление числа вызывает TypeError."""
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Cat", "Desc")
    with pytest.raises(TypeError):
        cat.add_product(42)


# ============ ИНТЕГРАЦИОННЫЕ ТЕСТЫ ============

def test_full_workflow():
    """Полный рабочий процесс."""
    Category.category_count = 0
    Category.product_count = 0
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


def test_new_product_and_add_to_category():
    """Тест создания товара через new_product."""
    Category.category_count = 0
    Category.product_count = 0
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
