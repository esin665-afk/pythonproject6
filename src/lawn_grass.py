"""
Модуль с классом LawnGrass.
"""

from src.product import Product


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
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
