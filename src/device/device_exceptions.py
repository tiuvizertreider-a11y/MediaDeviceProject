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
    """
    Ошибка некорректной категории устройства.

    :param category: Категория, которую мы получили от пользователя.
    :param correct_category: Допустимая категория значений.
    """

    def __init__(self, category: str, correct_category: list[str]):
        self.category = category
        self.correct_device = correct_category
        super().__init__(
            f"Недопустимая категория устройства: {self.category}. Допустимые значения: "
            f"{", ".join(correct_category)}."
        )


class InvalidYearDeviceError(DeviceError):
    """
    Ошибка некорректного года устройства.

    :param year: Год, который был передан пользователем.
    :param min_year: Минимальный возможный год устройства.
    :param max_year: Максимальный возможный год устройства.
    """
    def __init__(self, year: int, min_year: int, max_year: int):
        self.year = year
        self.min_year = min_year
        self.max_year = max_year
        super().__init__(
            f"Недопустимый год устройства: {self.year}. Допустимые года: "
            f"От {self.min_year} до {self.max_year}."
        )
