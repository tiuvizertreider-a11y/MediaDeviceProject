from abc import ABC, abstractmethod
from datetime import datetime

from ProjectClasses.review import Review


class Device(ABC):
    ALLOWED_CATEGORIES = ["Смартфоны", "Наушники", "Планшеты", "Умные часы"]   # Список для проверки.
    def __init__(self, brand: str, model: str, category: str,
                 year: int | None = None, image: str | None = None,
                 specs: dict | None = None, review: Review | None = None):
        self.brand = brand
        self.model = model
        self.category = category    # Обращение к сеттеру
        self.year = year            # Обращение к сеттеру
        self.image = image          # Обращение к сеттеру
        self.specs = specs          # Обращение к сеттеру
        self.review = review        # Обращение к сеттеру

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        if category not in self.ALLOWED_CATEGORIES:
            print('Категория должна быть одна из списка разрешенных категорий')
        else:
            self._category = category

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, new_year: int | None) -> None:
        if new_year is None:
            self._year = datetime.today().year
        elif not isinstance(new_year, int):
            print('Год выпуска устройства должен быть int | None')
        elif new_year < 1900 or new_year > datetime.today().year:
            print('Год выпуска устройства должен быть между 1900 года и настоящим временем')
        else:
            self._year = new_year

    @property
    def specs(self) -> dict:
        return self._specs.copy()

    @specs.setter
    def specs(self, new_specs: dict | None) -> None:
        if new_specs is None:
            self._specs = {}
        elif not isinstance(new_specs, dict):
            print('Список характеристик должен быть словарем')
        else:
            self._specs = new_specs.copy()

    @property
    def review(self) -> Review | None:
        return self._review

    @review.setter
    def review(self, new_review: Review | None) -> None:
        if new_review is None or isinstance(new_review, Review):
            self._review = new_review
        else:
            print('Новый обзор должен быть классом Review или None')

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, new_image: str | None) -> None:
        if new_image is None:
            self._image = '/'
        elif not isinstance(new_image, str):
            print('Новое изображение должно быть строкой')
        else:
            self._image = new_image


    @abstractmethod
    def get_device_type(self) -> str:
        pass

    @abstractmethod
    def get_short_description(self) -> str:
        pass
