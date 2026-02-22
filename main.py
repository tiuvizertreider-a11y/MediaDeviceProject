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
        self._is_on = False
        self.current_volume = current_volume

    # Геттеры
    @property
    def battery_level(self):
        return self._battery_level

    @property
    def is_on(self):
        return self._is_on

    @property
    def current_volume(self):
        return self._current_volume

    # Сеттеры
    @battery_level.setter
    def battery_level(self, battery_level):
        if 0 <= battery_level <= 100:
            self._battery_level = battery_level
        if battery_level <= 20:
            print('Предупреждение: уровень низкого заряда')


    @current_volume.setter
    def current_volume(self, current_volume):
        if self.MIN_VOLUME <= current_volume <= self.MAX_VOLUME:
            self._current_volume = current_volume
        else:
            print(f'{current_volume} - не установилось')

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
            self._is_on = True
        else:
            raise ValueError(f'Устройство: {self.brand} {self.model} уже включено')

    def power_off(self):
        """Выключить устройство"""
        if self.is_on:
            self._is_on = False
        else:
            raise ValueError(f'Устройство: {self.brand} {self.model} уже выключено')

    def charge(self):
        return 'Зарядить устройство'

    def adjust_volume(self, level):
        return 'Настроить громкость'

