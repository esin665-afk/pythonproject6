"""
Модуль с классом Category.
"""

from typing import List, Optional

from src.product import Product


class Category:
    """
    Класс для представления категории товаров.
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        if not isinstance(product, Product):
            raise TypeError(
                "В категорию можно добавлять только объекты класса "
                "Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self) -> float:
        """
        Рассчитывает средний ценник всех товаров в категории.

        Складывает только цены всех товаров и делит на их количество.
        Если товаров нет, возвращает 0.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в виде строки."""
        if not self.__products:
            return "В категории нет товаров"

        result = []
        for product in self.__products:
            result.append(str(product))

        return "\n".join(result)
