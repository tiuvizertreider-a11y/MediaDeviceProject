class Review:
    """
    -----Класс хранение информации об обзоре устройства-----
    :param title (str): Заголовок обзора
    :param content (str): Текст обзора
    :param date (datetime): Дата публикации (автоматически устанавливается в init)
    :param pros (list): Список плюсов
    :param cons (list): Список минусов
    :param author (str): Автор обзора
    """
    def __init__(self, title: str, content: str, date, pros=None, cons=None, author='Эксперт'):
        self.__title = title
        self.__content = content
        self.__date = date
        self.__pros = pros[:] if pros is not None else []
        self.__cons = cons[:] if cons is not None else []
        self.__author = author

    # Геттеры (для чтения всех атрибутов)
    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    @property
    def date(self):
        return self.__date

    @property
    def pros(self):
        return self.__pros[:]

    @property
    def cons(self):
        return self.__cons[:]

    @property
    def author(self):
        return self.__author

    def add_pro(self, pro_text):
        if len(pro_text) <= 200:
            self.__pros.append(pro_text)
        else:
            print(f'Текст плюса слишком длинный')

    def add_con(self, con_text):
        if len(con_text) <= 200:
            self.__cons.append(con_text)
        else:
            print(f'Текст минуса слишком длинный')

    def remove_pro(self, index):
        if index < 0 or index >= len(self.__pros):
            print('Индекс вне диапазона')
        else:
            del self.__pros[index]

    def remove_con(self, index):
        if index < 0 or index >= len(self.__cons):
            print('Индекс вне диапазона')
        else:
            del self.__cons[index]

    # В init параметры pros и cons могут быть None (тогда создаём пустые списки).
    # Присваиваем значения напрямую в приватные атрибуты.