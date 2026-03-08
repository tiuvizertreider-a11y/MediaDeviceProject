from datetime import datetime


class Review:
    """Модель Review для работы с отзывами"""

    def __init__(self, title: str, content: str, date: datetime=None,
                 pros: list[str]=None, cons: list[str]=None, author: str='Эксперт'):
        """
        Инициализирует объект отзыва.

        :param title:   Заголовок отзыва. Не может быть пустой строкой.
        :param content: Содержание (текст) отзыва.
        :param author:  Имя автора. По умолчанию 'Эксперт'.
        :param date: Дата и время создания. Если не указана,
                будет установлена текущая дата и время.
        :param pros: Список преимуществ.
                Если передан список, создаётся его копия. Если None, создаётся пустой список.
        :param cons: Список недостатков.
                Если передан список, создаётся его копия. Если None, создаётся пустой список.
        """
        self.__title = title
        self.__content = content
        self.__date = date if date is not None else datetime.now()
        self.__pros = pros.copy() if pros is not None else []
        self.__cons = cons.copy() if cons is not None else []
        self.__author = author

    # Геттеры (для чтения всех атрибутов)
    @property
    def title(self) -> str:
        """Возвращает название обзора"""
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        """Устанавливает значение для названия обзора"""
        self.__title = title

    @property
    def content(self) -> str:
        """Возвращает содержание обзора"""
        return self.__content

    @content.setter
    def content(self, content: str) -> None:
        """Устанавливает значение для содержания обзора"""
        self.__content = content

    @property
    def date(self) -> datetime:
        """Возвращает дату публикации"""
        return self.__date

    @date.setter
    def date(self, date: datetime) -> None:
        """Устанавливает значение для даты публикации"""
        self.__date = date

    @property
    def pros(self) -> list[str]:
        """Возвращает список плюсов"""
        return self.__pros.copy()

    @pros.setter
    def pros(self, pros: list[str]) -> None:
        """Устанавливает значение для списка плюсов"""
        self.__pros = pros

    @property
    def cons(self) -> list[str]:
        """Возвращает список минусов"""
        return self.__cons.copy()

    @cons.setter
    def cons(self, cons: list[str]) -> None:
        """Устанавливает значение для списка минусов"""
        self.__cons = cons

    @property
    def author(self) -> str:
        """Возвращает имя автора"""
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        """Устанавливает значение для имени автора"""
        self.__author = author

    def add_pro(self, pro_text: str) -> None:
        """
        Добавляет плюс в список плюсов и проверяет на валидность типа.
        :param pro_text: Новый плюс.
        :return: None.
        """
        if isinstance(pro_text, str):
            print(f'pro_text является экземпляром класса str')
        if len(pro_text) <= 200:
            self.__pros.append(pro_text)
        else:
            print(f'Текст плюса слишком длинный')

    def add_con(self, con_text: str) -> None:
        """
        Добавляет минус в список минусов и проверяет на валидность типа.
        :param con_text: Новый минус.
        :return: None.
        """
        if isinstance(con_text, str):
            print(f'con_text является экземпляром класса str')
        if len(con_text) <= 200:
            self.__cons.append(con_text)
        else:
            print(f'Текст минуса слишком длинный')

    def remove_pro(self, index: int) -> None:
        """
        Удаляет плюс из списка плюсов по индексу и проверяет на валидность типа.
        :param index: Индекс удаляемого элемента.
        :return: None.
        """
        if isinstance(index, int):
            print(f'index является экземпляром класса int')
        if -len(self.__pros) < index >= len(self.__pros):
            print('Индекс вне диапазона')
        else:
            del self.__pros[index]

    def remove_con(self, index: int) -> None:
        """
        Удаляет минус из списка минусов по индексу и проверяет на валидность типа.
        :param index: Индекс удаляемого элемента.
        :return: None.
        """
        if isinstance(index, int):
            print(f'index является экземпляром класса int')
        if -len(self.__cons) < index >= len(self.__cons):
            print('Индекс вне диапазона')
        else:
            del self.__cons[index]
