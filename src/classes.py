"""
Модуль с основными классами для интернет-магазина.
Содержит классы Product и Category для работы с товарами и категориями.
"""

from typing import List, Optional


class Product:
    """
    Класс для представления товара.
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Инициализация объекта товара с проверкой данных.
        """
        if price <= 0:
            raise ValueError("Цена товара должна быть больше 0")
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        Строковое представление товара.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Магический метод сложения двух товаров.
        """
        if type(self) is not type(other):
            raise TypeError(
                "Нельзя складывать товары разных классов: "
                f"{type(self).__name__} и {type(other).__name__}"
            )
        return (self.price * self.quantity) + (other.price * other.quantity)

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

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """
        Класс-метод для создания продукта из словаря с данными.
        """
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
