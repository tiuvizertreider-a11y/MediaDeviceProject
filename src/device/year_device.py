from datetime import datetime
from enum import StrEnum

from src.device.device_exceptions import InvalidYearDeviceError


class YearDevice(StrEnum):
    """
    Инициализирует год устройства.

    :param year: Год, который был передан пользователем,
            если год передан корректно = инициализирует,
            иначе = поднимет исключение InvalidYearDeviceError.
    """
    def __init__(self, year):
        self.year = year

        if self.year < 1990 or self.year > datetime.today().year:
            self.year = datetime.today().year
        else:
            raise InvalidYearDeviceError

    @staticmethod
    def to_list() -> list[str]:
        """Возвращает значения YearDevice."""
        return [i for i in YearDevice]
