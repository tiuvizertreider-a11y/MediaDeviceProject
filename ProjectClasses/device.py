from abc import ABC, abstractmethod
from datetime import datetime

from pyexpat import model

from unicodedata import category

from ProjectClasses.review import Review


class Device(ABC):
    ALLOWED_CATEGORIES = ["Смартфоны", "Наушники", "Планшеты", "Умные часы"]   # Список для проверки.
    def __init__(self, brand: str, model: str, category: str,
                 year: int | None = None, image: str | None = None,
                 specs: dict | None = None, review: Review | None = None):
        """
        Инициализирует объект устройства.


        :param brand:    Бренд устройства. Не может быть пустой строкой.
        :param model:    Модель устройства. Не может быть пустой строкой.
        :param category: Категория устройства. Категория должна быть
                одна из списка разрешенных устройств.
        :param year:     Год выпуска устройства. Год выпуска устройства
                должен быть между 1900 года и настоящим временем.
                если будет передано None = будет использован текущий год.
        :param image: Изображение устройства. Если будет передано
                None = подставится ссылка, с фотокарточкой по умолчанию.
        :param specs: Характеристики устройства. Список характеристик
                должен быть словарем. Если передано None = создаст {}.
        :param review: Сам обзор эксперта. Новый обзор должен быть
                классом Review или None.
        """
        self.brand = brand
        self.model = model
        self.category = category    # Обращение к сеттеру
        self.year = year            # Обращение к сеттеру
        self.image = image          # Обращение к сеттеру
        self.specs = specs          # Обращение к сеттеру
        self.review = review        # Обращение к сеттеру

    @property
    def category(self) -> str:
        """Возвращает категорию устройства."""
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Устанавливает значение для категории устройства.
        :param category: Категория из списка разрешенных категорий.
        :return: None.
        """
        if category not in self.ALLOWED_CATEGORIES:
            print('Категория должна быть одна из списка разрешенных категорий')
        else:
            self._category = category

    @property
    def year(self) -> int:
        """Возвращает год выпуска устройства."""
        return self._year

    @year.setter
    def year(self, new_year: int | None) -> None:
        """
        Устанавливает значение для года выпуска устройства.
        Если передано None, то установится текущий год.
        :param new_year: Год выпуска устройства.
        :return: None.
        """
        if new_year is None:
            self._year = datetime.today().year
        elif not isinstance(new_year, int):
            print('Год выпуска устройства должен быть int | None')
        elif new_year < 1900 or new_year > datetime.today().year:
            print('Год выпуска устройства должен быть между 1900 года и настоящим временем')
        else:
            self._year = new_year

    @property
    def image(self) -> str:
        """Возвращает изображение устройства."""
        return self._image

    @image.setter
    def image(self, new_image: str | None) -> None:
        """
        Устанавливает значение для изображения устройства.
        Если передано None, то подставится ссылка, с фотокарточкой
            по умолчанию.
        :param new_image: Изображение устройства.
        :return: None.
        """
        if new_image is None:
            self._image = '/'
        elif not isinstance(new_image, str):
            print('Новое изображение должно быть строкой')
        else:
            self._image = new_image

    @property
    def specs(self) -> dict:
        """Возвращает характеристики устройства."""
        return self._specs.copy()

    @specs.setter
    def specs(self, new_specs: dict | None) -> None:
        """
        Устанавливает значение для характеристик устройства.
        Если передано None, то создаст пустой словарь {}.
        :param new_specs: Новые характеристики.
        :return: None.
        """
        if new_specs is None:
            self._specs = {}
        elif not isinstance(new_specs, dict):
            print('Список характеристик должен быть словарем')
        else:
            self._specs = new_specs.copy()

    @property
    def review(self) -> Review | None:
        """Возвращает обзор на устройство."""
        return self._review

    @review.setter
    def review(self, new_review: Review | None) -> None:
        """
        Устанавливает значение для обзора на устройство.
        Если передано None, то атрибут _review инициализируется.
        :param new_review: Новый обзор.
        :return: None.
        """
        if new_review is None or isinstance(new_review, Review):
            self._review = new_review
        else:
            print('Новый обзор должен быть классом Review или None')


    @abstractmethod
    def get_device_type(self) -> str:
        pass

    @abstractmethod
    def get_short_description(self) -> str:
        pass

    def __repr__(self) -> str:
        """Возвращает отчет об объекте."""
        return (f'Device(brand={self.brand}, model={self.model}, category={self.category},'
                f'year={self.year}, image={self.image}, specs={self.specs}, review={self.review})')

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return (f'Info device:\n\tbrand={self.brand}\n\tmodel={self.model}'
                f'\n\tcategory={self.category}\n\tyear={self.year}'
                f'\n\timage={self.image}\n\tspecs={self.specs}\n\treview={self.review}')

    @classmethod
    def from_dict(cls, data: dict) -> Device | None:
        """
        Создаёт экземпляр класса Device из словаря.
        :param data: Словарь с ключами: brand, model,
            category (обязательные), year, image, specs,
            review (опционально).
        :return: Возвращает устройство или None.
        """
        if not isinstance(data, dict):
            print(f'data должен быть словарем!')
            return None

        base_keys = ['brand', 'model', 'category']
        for key in base_keys:
            if key not in data:
                print(f'Ключ должен быть из списка базовых ключей.')
                return None

        return cls(
            brand=data['brand'],
            model=data['model'],
            category=data['category'],
            year=data.get('year'),
            image=data.get('image'),
            specs=data.get('specs'),
            review=data.get('review')
        )
