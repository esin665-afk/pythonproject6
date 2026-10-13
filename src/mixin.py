"""
Модуль с классом-миксином для логирования создания объектов.
"""


class ReprMixin:
    """
    Класс-миксин для вывода информации о создании объекта.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализация миксина.
        """
        # Формируем строку с параметрами
        params = ", ".join(repr(arg) for arg in args)
        print(f"{type(self).__name__}({params})")

        # Вызываем родительский конструктор
        super().__init__(*args, **kwargs)
