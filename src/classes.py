"""
Модуль с основными классами для интернет-магазина.
"""

from typing import List, Optional

from src.base_product import BaseProduct
from src.mixin import ReprMixin


class Product(ReprMixin, BaseProduct):  # ← Миксин ПЕРВЫМ в цепочке
    """
    Класс для представления товара.
    Наследник BaseProduct с миксином ReprMixin.
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализация товара."""
        super().__init__(name, description, price, quantity)

    # ... остальные методы без изменений

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """Магический метод сложения двух товаров одного класса."""
        if type(self) is not type(other):
            raise TypeError(
                "Нельзя складывать товары разных классов: "
                f"{type(self).__name__} и {type(other).__name__}"
            )
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Класс-метод для создания продукта из словаря."""
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')
        return cls(name, description, price, quantity)


class Smartphone(Product):
    """
    Класс для представления смартфона.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализация смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для представления газонной травы.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализация газонной травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """
    Класс для представления категории товаров.
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        """
        Инициализация категории.
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """
        Строковое представление категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return (
            f"{self.name}, количество продуктов: "
            f"{total_quantity} шт."
        )

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.
        """
        if not isinstance(product, Product):
            raise TypeError(
                "В категорию можно добавлять только объекты класса "
                "Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Рассчитывает среднюю цену товаров в категории.
        """
        if not self.__products:
            raise ValueError("Нет товаров в категории для расчета средней цены")

        total_price = sum(product.price for product in self.__products)
        return total_price / len(self.__products)

    @property
    def products(self) -> str:
        """
        Геттер для получения списка товаров в виде строки.
        """
        if not self.__products:
            return "В категории нет товаров"

        result = []
        for product in self.__products:
            result.append(str(product))

        return "\n".join(result)
