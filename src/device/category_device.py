from enum import StrEnum


class CategoryDevice(StrEnum):
    """Инициализирует категорию устройства."""
    SMARTPHONE = "smartphone"
    HEADPHONE = "headphone"
    TABLET = "tablet"
    SMARTWATCH = "smartwatch"

    @staticmethod
    def to_list() -> list[str]:
        """Возвращает список значений CategoryDevice."""
        return [i.value for i in CategoryDevice]
