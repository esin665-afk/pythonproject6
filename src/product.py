"""
Модуль с классом Product.
"""

from src.base_product import BaseProduct
from src.mixin import ReprMixin


class Product(ReprMixin, BaseProduct):
    """
    Класс для представления товара.
    Наследник BaseProduct с миксином ReprMixin.
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализация товара."""
        super().__init__(name, description, price, quantity)

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
