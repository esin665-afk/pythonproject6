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
        __price (float): Приватная цена товара (с копейками)
        quantity (int): Количество товара в наличии (в штуках)
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Инициализация объекта товара с проверкой данных.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара (должна быть > 0)
            quantity: Количество на складе (должно быть >= 0)

        Raises:
            ValueError: Если цена <= 0 или количество < 0
        """
        if price <= 0:
            raise ValueError("Цена товара должна быть больше 0")
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для получения цены товара."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для установки цены товара с проверкой.

        Args:
            value: Новая цена товара

        Если цена <= 0, выводит сообщение об ошибке и не меняет цену.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """
        Класс-метод для создания продукта из словаря с данными.

        Args:
            product_data (dict): Словарь с ключами 'name', 'description', 'price', 'quantity'

        Returns:
            Product: Созданный объект Product
        """
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')
        return cls(name, description, price, quantity)


class Category:
    """
    Класс для представления категории товаров.

    Атрибуты класса:
        category_count (int): Общее количество созданных категорий
        product_count (int): Общее количество товаров во всех категориях

    Атрибуты экземпляра:
        name (str): Название категории
        description (str): Описание категории
        __products (List[Product]): Приватный список товаров в категории
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
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.

        Args:
            product: Объект Product для добавления
        """
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Рассчитывает среднюю цену товаров в категории.

        Returns:
            float: Средняя цена товаров в категории

        Raises:
            ValueError: Если в категории нет товаров
        """
        if not self.__products:
            raise ValueError("Нет товаров в категории для расчета средней цены")

        total_price = sum(product.price for product in self.__products)
        return total_price / len(self.__products)

    @property
    def products(self) -> str:
        """
        Геттер для получения списка товаров в виде строки.

        Returns:
            str: Строка с информацией о товарах в формате:
                 "Название продукта, X руб. Остаток: Y шт."
        """
        if not self.__products:
            return "В категории нет товаров"

        result = []
        for product in self.__products:
            result.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )

        return "\n".join(result)
