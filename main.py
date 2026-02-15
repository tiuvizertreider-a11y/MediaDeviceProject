from abc import ABC, abstractmethod

class MediaDevice(ABC):
    MAX_VOLUME = 100         # Максимальная громкость (константа)
    MIN_VOLUME = 0           # Минимальная громкость (константа)
    BATTERY_WARNING_LEVEL = 20             # Уровень предупреждения о разрядке
    manufacturer_country = "Russia"        # Страна производства (может переопределяться в дочерних классах)

    def __init__(self, brand, model, battery_level, current_volume):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_on = False
        self.current_volume = current_volume

    # Геттеры
    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def battery_level(self):
        return self.__battery_level

    @property
    def is_on(self):
        return self.__is_on

    @property
    def current_volume(self):
        return self.__current_volume

    # Сеттеры
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @model.setter
    def model(self, model):
        self.__model = model

    @battery_level.setter
    def battery_level(self, battery_level):
        self.__battery_level = battery_level

    @is_on.setter
    def is_on(self, is_on):
        self.__is_on = is_on

    @current_volume.setter
    def current_volume(self, current_volume):
        self.__current_volume = current_volume

    # Абстрактные методы
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get_device_type(self):
        pass

    # Обычные методы класса (экземпляра)
    def power_on(self):
        """Включить устройство"""
        if not self.is_on:
            self.is_on = True
            print(f'Устройство: {self.brand} {self.model} включено')
        else:
            print(f'Устройство: {self.brand} {self.model} уже включено')

    def power_off(self):
        """Выключить устройство"""
        if self.is_on:
            self.is_on = False
            print(f'Устройство: {self.brand} {self.model} включено')
        else:
            print(f'Устройство: {self.brand} {self.model} уже включено')

    def charge(self):
        return 'Зарядить устройство'

    def adjust_volume(self, level):
        return 'Настроить громкость'