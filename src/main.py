"""
Модуль с основными классами для интернет-магазина.
Содержит классы Product и Category для работы с товарами и категориями.
"""

from typing import List, Optional


class Product:
    """
    Класс для представления товара.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара (с копейками)
        quantity (int): Количество товара в наличии (в штуках)
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Инициализация объекта товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров.

    Атрибуты класса:
        category_count (int): Общее количество созданных категорий
        product_count (int): Общее количество товаров во всех категориях

    Атрибуты экземпляра:
        name (str): Название категории
        description (str): Описание категории
        products (List[Product]): Список товаров в категории
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров (по умолчанию пустой список)
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)
