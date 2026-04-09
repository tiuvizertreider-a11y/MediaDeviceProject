from src.review.status_review import StatusReview


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
    # TODO: РЕАЛИЗОВАТЬ ДОКУМЕНТАЦИЮ! 🐞

    def __init__(self, status: str, correct_status: list[str]):
        self.status = status
        self.correct_status = correct_status
        super().__init__(
            f"Недопустимый статус: {self.status}. Допустимые значения: "
            f"{", ".join(correct_status)}."
        )