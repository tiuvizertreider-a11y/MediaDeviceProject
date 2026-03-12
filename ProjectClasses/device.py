from abc import ABC, abstractmethod

class Device(ABC):
    ALLOWED_CATEGORIES = ["Смартфоны", "Наушники", "Планшеты", "Умные часы"]   # Список для проверки.
    def __init__(self, brand: str, model: str, category: str,
                 year: int | None = None, image: str | None = None,
                 specs: dict | None = None, review: Review | None = None):
        self.brand = brand
        self.model = model
        self._category = category
        self._year = year
        self._image = image
        self._specs = specs
        self._review = review

    @abstractmethod
    def get_device_type(self) -> str:
        pass

    @abstractmethod
    def get_short_description(self) -> str:
        pass
