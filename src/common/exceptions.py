class AppError(Exception):
    """Базовое исключение для всех ожидаемых ошибок приложения."""

    pass


class ValidationError(AppError):
    """Базовое исключение для ошибок валидации данных."""

    pass


class EmptyFieldError(ValidationError):
    """
    Поле не может быть пустым (пустая строка или строка из пробелов).

    :param field_name: Имя поля.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.
    """

    def __init__(self, field_name: str, entity: str):
        self.field_name = field_name
        self.entity = entity
        super().__init__(
            f"Поле: '{self.entity}.{self.field_name}' - не может быть пустым!"
        )


class TextTooLongError(ValidationError):
    """
    Текстовое поле превышает допустимую длину.

    :param value: Переданное значение пользователем.
    :param field_name: Имя поля.
    :param max_length: Максимальная длина поля.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.
    """

    def __init__(self, value: str, field_name: str, max_length: int, entity: str):
        self.value = value
        self.field_name = field_name
        self.max_length = max_length
        self.entity = entity
        super().__init__(
            f"Поле: '{self.entity}.{self.field_name}' - превышена"
            f" максимальная длина. Текущая длина: {self.value}. Максимальная: 200."
        )


class MissingRequiredFieldError(ValidationError):
    """
    В словаре отсутствует обязательное поле.

    :param field_name: Имя поля.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.
    """
    def __init__(self, field_name: str, entity: str):
        self.field_name = field_name
        self.entity = entity
        super().__init__(
            f"Поле: '{self.entity}.{self.field_name}'- отсутствует"
            f" обязательное поле 'Review.title'."
        )


class InvalidChoiceError(ValidationError):
    """
    Значение не входит в список допустимых значений.

    :param value: Переданное значение пользователем.
    :param field_name: Имя поля.
    :param allowed: Список разрешенного - тип данных: str.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.
    """
    def __init__(self, value: str, field_name: str, allowed: list[str], entity: str):
        self.value = value
        self.field_name = field_name
        self.allowed = allowed
        self.entity = entity
        super().__init__(
        f"В поле: '{self.entity}.{self.field_name}' - недопустимое"
        f" значение 'Review.status: unknown'. Допустимые: '{self.allowed}'."
    )


class YearOutOfRangeError(ValidationError):
    """
    Год выходит за допустимый диапазон.

    :param year: Год, переданный пользователем.
    :param start_year: Минимальный возможный год.
    :param end_year: Максимальный возможный год.
    :param field_name: Имя поля.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.
    """
    def __init__(self, year: int, start_year: int, end_year: int, field_name: str, entity: str):
        self.year = year
        self.start_year = start_year
        self.end_year = end_year
        self.field_name = field_name
        self.entity = entity
        super().__init__(
        f"Переданный год: '{self.year}' не попадает в допустимый"
        f" диапазон: {self.start_year}-{self.end_year}."
    )