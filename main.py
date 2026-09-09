"""
Проверочный файл для демонстрации работы классов.
Запустите: python main.py
"""

from src.classes import Product, Category


if __name__ == "__main__":
    print("=" * 60)
    print("ПРОВЕРКА РАБОТЫ КЛАССОВ PRODUCT И CATEGORY")
    print("=" * 60)

    # ===== 1. СОЗДАНИЕ ТОВАРОВ =====
    print("\n1. СОЗДАНИЕ ТОВАРОВ:")
    print("-" * 60)

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    print(f"✓ Создан: {product1.name}")

    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
    print(f"✓ Создан: {product2.name}")

    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )
    print(f"✓ Создан: {product3.name}")

    # ===== 2. СОЗДАНИЕ КАТЕГОРИИ =====
    print("\n2. СОЗДАНИЕ КАТЕГОРИИ:")
    print("-" * 60)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    print(f"✓ Создана категория: {category1.name}")
    print(f"  Количество товаров: {len(category1._Category__products)}")

    # ===== 3. ВЫВОД ТОВАРОВ ЧЕРЕЗ ГЕТТЕР =====
    print("\n3. ТОВАРЫ В КАТЕГОРИИ (ГЕТТЕР):")
    print("-" * 60)
    print(category1.products)

    # ===== 4. ДОБАВЛЕНИЕ НОВОГО ТОВАРА =====
    print("\n4. ДОБАВЛЕНИЕ НОВОГО ТОВАРА:")
    print("-" * 60)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(f"✓ Добавлен: {product4.name}")
    print(f"  Всего товаров в категории: {category1.product_count}")

    print("\n   Обновленный список товаров:")
    print(category1.products)

    # ===== 5. КЛАСС-МЕТОД NEW_PRODUCT =====
    print("\n5. КЛАСС-МЕТОД NEW_PRODUCT (СОЗДАНИЕ ИЗ СЛОВАРЯ):")
    print("-" * 60)

    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    new_product = Product.new_product(new_product_data)
    print("✓ Товар создан через класс-метод new_product:")
    print(f"   Название: {new_product.name}")
    print(f"   Описание: {new_product.description}")
    print(f"   Цена: {new_product.price} руб.")
    print(f"   Количество: {new_product.quantity} шт.")

    # ===== 6. ПРОВЕРКА ГЕТТЕРА И СЕТТЕРА ЦЕНЫ =====
    print("\n6. ПРОВЕРКА ГЕТТЕРА И СЕТТЕРА ЦЕНЫ:")
    print("-" * 60)

    test_product = Product("Тестовый товар", "Для проверки цены", 1000.0, 1)
    print(f"✓ Начальная цена: {test_product.price} руб.")

    # Устанавливаем корректную цену
    test_product.price = 1500.0
    print(f"✓ Установлена новая цена (1500): {test_product.price} руб.")

    # Пытаемся установить отрицательную цену
    print("\n   Попытка установить отрицательную цену (-500):")
    test_product.price = -500.0  # Должно вывести ошибку
    print(f"   Цена после попытки: {test_product.price} руб. (не изменилась)")

    # Пытаемся установить нулевую цену
    print("\n   Попытка установить нулевую цену (0):")
    test_product.price = 0  # Должно вывести ошибку
    print(f"   Цена после попытки: {test_product.price} руб. (не изменилась)")

    # ===== 7. СТАТИСТИКА =====
    print("\n7. СТАТИСТИКА:")
    print("-" * 60)
    print(f"✓ Всего категорий: {Category.category_count}")
    print(f"✓ Всего товаров: {Category.product_count}")

    print("\n" + "=" * 60)
    print("ПРОВЕРКА ЗАВЕРШЕНА УСПЕШНО! 🎉")
    print("=" * 60)
