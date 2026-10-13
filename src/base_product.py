"""
Модуль с абстрактным базовым классом для всех продуктов.
"""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Инициализация базового продукта.
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
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения."""
        pass
