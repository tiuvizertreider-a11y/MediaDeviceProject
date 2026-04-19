from enum import StrEnum
from typing import Callable


class CategoryDevice(StrEnum):
    """Инициализирует категорию устройства."""
    SMARTPHONE = "Смартфоны"
    HEADPHONE = "Наушники"
    TABLET = "Планшеты"
    SMARTWATCH = "Умные часы"

    @staticmethod
    def to_list() -> list[Callable[[], str]]:
        """Возвращает список значений CategoryDevice."""
        return [i.value for i in CategoryDevice]
    