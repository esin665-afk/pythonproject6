"""
Интеграционные тесты.
"""

from src import Category, Product


def test_full_workflow():
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
    assert category.middle_price() == 40000.0
    assert Category.product_count == 2


def test_new_product_and_add_to_category():
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
