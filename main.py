from abc import ABC, abstractmethod

class MediaDevice(ABC):
    MAX_VOLUME = 100         # Максимальная громкость (константа)
    MIN_VOLUME = 0           # Минимальная громкость (константа)
    BATTERY_WARNING_LEVEL = 20             # Уровень предупреждения о разрядке
    manufacturer_country = "Russia"        # Страна производства (может переопределяться в дочерних классах)

    def __init__(self, brand, model, battery_level, is_on, current_volume):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_on = is_on
        self.current_volume = current_volume



