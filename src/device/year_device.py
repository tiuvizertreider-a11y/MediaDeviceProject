from datetime import datetime

from src.device.device_exceptions import InvalidYearDeviceError


class YearDevice:

    def __init__(self, year: int, min_year: int=1990, max_year: int=datetime.now().year):
        self.year = year
        self.min_year = min_year
        self.max_year = max_year

        if min_year > year > max_year:
            raise InvalidYearDeviceError

        self.year = year