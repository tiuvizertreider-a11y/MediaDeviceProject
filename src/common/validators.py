from src.common.exceptions import (
    EmptyFieldError,
    TextTooLongError,
    YearOutOfRangeError)


def validate_non_empty_string(
        value: str,
        field_name: str,
        entity: str,
) -> str:
    """
    Проверяет, что переданное значение:
    является типом данных string
    не является пустой строкой
    не состоит только из пробелов

    :param value: Переданное значение (string).
    :param field_name: Имя поля.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.

    :return: Normalized, если все проверки прошли
        (С автоматической обрезкой пробелов).


    :raises TypeError: Если value не является строкой.
    :raises EmptyFieldError: Если строка пустая или состоит только из пробелов.
    """
    if not isinstance(value, str):
        raise TypeError(
            f'В поле: {field_name}-{entity} ожидается тип данных: str.\n'
            f'Получен: "{type(value).__name__}"'
        )
    if value == '' or value is ' ':
        raise EmptyFieldError(field_name, entity)

    normalized = value.strip()
    if not normalized:
        raise EmptyFieldError(field_name, entity)

    return normalized


def validate_string_length(
    text: str,
    field_name: str,
    max_length: int,
    entity: str,
) -> str:
    """
    Проверяет, что переданный текст (string):
    не пустая
    не длиннее max_length

    :param text: Переданный текст (string).
    :param field_name: Имя поля.
    :param max_length: Максимальная длина поля.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.

    :return: Normalized, если все проверки прошли
        (С автоматической обрезкой пробелов).

    :raises EmptyFieldError: Если переданный текст пустой или
        состоит только из пробелов.
    :raises TextTooLongError: Если длина переданного текста
        больше максимальной длины поля.
    :raises EmptyFieldError: Если до этого две проверки не прошли,
        в normalized не сохранится text.strip().
    """
    if text == '' or text is ' ':
        raise EmptyFieldError(field_name, entity)
    if len(text) > max_length:
        raise TextTooLongError(text, field_name, max_length, entity)

    normalized = text.strip()
    if not normalized:
        raise EmptyFieldError(field_name, entity)

    return normalized


def validate_range_year(
    year: int,
    start_year: int,
    end_year: int,
    field_name: str,
    entity: str,
) -> int:
    """
    Проверяет, что переданный год:
    является типом данных integer
    входит в диапазон годов

    :param year: Переданный год (integer).
    :param start_year: Минимально возможный год.
    :param end_year: Максимально возможный год.
    :param field_name: Имя поля.
    :param entity: Имя сущности (класса), к которой относится поле
        и где произошла ошибка.

    :return: Year, если все проверки прошли.

    :raises TypeError: Если переданный год не является integer.
    :raises YearOutOfRangeError: Если переданный год выходит из диапазона.
    """
    if not isinstance(year, int):
        raise TypeError(
            f'В поле: {field_name}-{entity} ожидается тип данных: int.\n'
            f'Получен: "{type(year).__name__}"'
        )
    if year < start_year or year > end_year:
        raise YearOutOfRangeError(year, start_year, end_year, field_name, entity)

    return year