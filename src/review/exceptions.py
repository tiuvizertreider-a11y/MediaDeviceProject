class ReviewError(Exception):
    """Базовое исключение для всех ошибок, связанных с Review."""

    pass


class EmptyFieldReviewError(ReviewError):
    """
    Исключение, возникающее при попытке установить пустое значение в обязательное поле.

    :param field_name: Имя поля, которое не должно быть пустым.
    """

    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(f"Поле: {self.field_name} не может быть пустым!")


class InvalidStatusReviewError(ReviewError):
    """
    Ошибка некорректного статуса обзора.

    :param status: Статус, переданный пользователем.
    :param correct_status: Список корректных значений.
    """

    def __init__(self, status: str, correct_status: list[str]):
        self.status = status
        self.correct_status = correct_status
        super().__init__(
            f"Недопустимый статус: {self.status}. Допустимые значения: "
            f"{", ".join(correct_status)}."
        )


class IncorrectLengthFieldReviewError(ReviewError):
    """
    Ошибка некорректной длины поля обзора.

    :param field_name: Имя поля, переданное пользователем.
    :param length: Текущая длина поля.
    :param max_length: Максимальная длина поля.
    """

    def __init__(self, field_name: str, length: int, max_length: int):
        self.field_name = field_name
        self.length = length
        self.max_length = max_length
        super().__init__(
            f"Превышена максимальная длина поля {self.field_name} - {self.max_length} символов!"
            f"Текущая длина: {self.length}."
        )


class MissingRequiredFieldReviewError(ReviewError):
    """
    Ошибка пропущенного обязательного поля обзора.

    :param field_name: Имя поля, переданное пользователем.
    """

    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(f"Пропущено обязательное поле: {self.field_name}.")
