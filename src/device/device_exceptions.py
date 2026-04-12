from src.device.category_device import CategoryDevice


class DeviceError(Exception):
    """Базовое исключение для всех ошибок, связанных с Device."""
    pass


class EmptyFieldDeviceError(DeviceError):
    """
    Исключение, возникающее при попытке установить пустое значение в обязательное поле.

    :param field_name: Имя поля, которое не должно быть пустым.
    """

    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(
            f"Поле: {self.field_name} не может быть пустым!"
        )


class InvalidCategoryDeviceError(DeviceError):
    """Ошибка некорректной категории устройства."""

    def __init__(self, category: str, correct_category: list[str]):
        self.category = category
        self.correct_device = correct_category
        super().__init__(
            f"Недопустимая категория устройства: {self.category}. Допустимые значения: "
            f"{", ".join(correct_category)}."
        )