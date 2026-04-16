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
        super().__init__(
            f"Поле: {self.field_name} не может быть пустым!"
        )


class InvalidStatusReviewError(ReviewError):
    """Ошибка некорректного статуса обзора."""

    def __init__(self, status: str, correct_status: list[str]):
        self.status = status
        self.correct_status = correct_status
        super().__init__(
            f"Недопустимый статус: {self.status}. Допустимые значения: "
            f"{", ".join(correct_status)}."
        )

class IncorrectLengthFiledReviewError(ReviewError):
    # TODO: ДОКУМЕНТАЦИЯ
    def __init__(self, field_name: str, length: int, max_length: int):
        self.field_name = field_name
        self.length = length
        self.max_length = max_length
        super().__init__(
            f"Превышена максимальная длина поля {self.field_name} - {self.max_length} символов!"
            f"Текущая длина: {self.length}."
        )


class MissingRequiredFieldReviewError(ReviewError):
    # TODO: ДОКУМЕНТАЦИЯ
    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(
            f"Пропущено обязательное поле: {self.field_name}."
        )