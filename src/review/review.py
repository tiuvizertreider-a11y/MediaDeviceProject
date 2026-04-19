from datetime import datetime
from typing import TypedDict, Required, Self

from src.review.status_review import StatusReview
from src.review.review_exceptions import InvalidStatusReviewError, EmptyFieldReviewError, \
    IncorrectLengthFieldReviewError, MissingRequiredFieldReviewError


class ReviewData(TypedDict, total=False):
    """🍩✅⛹️☠️⬆️🧐"""
    # TODO: ДОКУМЕНТАЦИЯ
    title: Required[str]
    content: Required[str]
    status: StatusReview | str
    date: datetime | None
    pros: list[str] | None
    cons: list[str] | None
    author: str


class Review:
    """Модель Review для работы с отзывами."""

    def __init__(self,
                 title: str,
                 content: str,
                 status: StatusReview | str = StatusReview.PUBLISHED,
                 date: datetime=None,
                 pros: list[str]=None,
                 cons: list[str]=None,
                 author: str='Эксперт',
                 ):
        """
        Инициализирует объект отзыва.

        :param title:   Заголовок отзыва. Не может быть пустой строкой.
        :param content: Содержание (текст) отзыва.
        :param status:  Статус обзора. Статус должен быть
                один из класса StatusReview.
        :param author:  Имя автора. По умолчанию 'Эксперт'.
        :param date: Дата и время создания. Если не указана,
                будет установлена текущая дата и время.
        :param pros: Список преимуществ.
                Если передан список, создаётся его копия. Если None, создаётся пустой список.
        :param cons: Список недостатков.
                Если передан список, создаётся его копия. Если None, создаётся пустой список.
        """
        # Присваиваем через свойства
        self.title = title
        self.content = content
        self.status = status
        self.date = date
        self.pros = pros
        self.cons = cons
        self.author = author

    # Геттеры (для чтения всех атрибутов)
    @property
    def title(self) -> str:
        """Возвращает название обзора."""
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        """
        Устанавливает значение для названия обзора.
        :param title: Новое название обзора.
        :raises ValueError: Если title не str.
        :return: None.
        """
        if not isinstance(title, str):
            raise ValueError('title должен быть str.')
        
        self.__title = title

    @property
    def content(self) -> str:
        """Возвращает содержание обзора."""
        return self.__content

    @content.setter
    def content(self, content: str) -> None:
        """
        Устанавливает значение для содержания обзора.
        :param content: Новое содержание обзора.
        :raises ValueError: Если content не str.
        :return: None.
        """
        if not isinstance(content, str):
            raise ValueError('content должен быть str.')

        self.__content = content

    @property
    def status(self) -> StatusReview:
        """Возвращает статус обзора."""
        return self.__status

    @status.setter
    def status(self, status: StatusReview | str) -> None:
        """
        Инициализирует и проверяет на корректность статуса.
        :param status: Должен быть одним из класса StatusReview.
        :raises InvalidStatusReviewError: TODO: описать
        :return: None.
        """
        try:
            self.__status = StatusReview(status)
        except ValueError as ex:
            cor_status = StatusReview.to_list()
            raise InvalidStatusReviewError(status, cor_status) from ex

    @property
    def date(self) -> datetime:
        """Возвращает дату публикации."""
        return self.__date

    @date.setter
    def date(self, new_date: datetime | None) -> None:
        """
        Устанавливает значение для даты публикации.
        Если будет передано None, то присвоит текущую дату.
        :param new_date: Новая дата.
        :raises ValueError: TODO: Описать
        :return: None.
        """
        if new_date is None:
            self.__date = datetime.now()
        elif isinstance(new_date, datetime):
            self.__date = datetime
        else:
            raise ValueError('Дата публикации должна быть datetime.')

    @property
    def pros(self) -> list[str]:
        """Возвращает список плюсов."""
        return self.__pros.copy()

    @pros.setter
    def pros(self, pros: list[str] | None) -> None:
        """
        Устанавливает значение для списка плюсов.
        Если будет передано None, то присвоит пустой список.
        :param pros: Новый список плюсов.
        :raises ValueError: TODO: Описать
        :return: None.
        """
        if pros is None:
            self.__pros = []
        elif isinstance(pros, list):
            self.__pros = pros.copy()
        else:
            raise ValueError('Список плюсов должно быть list.')

    @property
    def cons(self) -> list[str]:
        """Возвращает список минусов."""
        return self.__cons.copy()

    @cons.setter
    def cons(self, cons: list[str] | None) -> None:
        """
        Устанавливает значение для списка минусов.
        Если будет передано None, то присвоит пустой список.
        :param cons: Новый список минусов.
        :raises ValueError: TODO: Описать
        :return: None.
        """
        if cons is None:
            self.__cons = []
        elif isinstance(cons, list):
            self.__cons = cons.copy()
        else:
            raise ValueError('Список минусов должно быть списком.')

    @property
    def author(self) -> str:
        """Возвращает имя автора."""
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        """
        Устанавливает значение для имени автора.
        :param author: Автор обзора. По умолчанию = Эксперт.
        :raises ValueError: TODO: Описать
        :return: None.
        """
        if not isinstance(author, str):
            raise ValueError('Имя автора должно быть строкой.')

        self.__author = author


    def add_pro(self, pro_text: str, max_length: int=200) -> None:
        """
        Добавляет плюс в список плюсов и проверяет на валидность типа.
        :param pro_text: Новый плюс.
        :param max_length: Максимальная длина поля.
        :raises ValueError: TODO: ОПИСАНИЕ
        :raises EmptyFieldReviewError: TODO: ОПИСАНИЕ
        :raises IncorrectLengthFiledReviewError: TODO: ОПИСАНИЕ
        :return: None.
        """
        self.__validate_text(pro_text, "pro_text", max_length)
        self.__pros.append(pro_text)

    def add_con(self, con_text: str, max_length: int=200) -> None:
        """
        Добавляет минус в список минусов и проверяет на валидность типа.
        :param con_text: Новый минус.
        :param max_length: Максимальная длина поля.
        :raises ValueError: TODO: ОПИСАНИЕ
        :raises EmptyFieldReviewError: TODO: ОПИСАНИЕ
        :raises IncorrectLengthFiledReviewError: TODO: ОПИСАНИЕ
        :return: None.
        """
        self.__validate_text(con_text, "con_text", max_length)
        self.__pros.append(con_text)

    @staticmethod
    def __validate_text(text: str, field_name: str, max_length: int):
        # TODO: ДОКУМЕНТАЦИЯ
        if not isinstance(text, str):
            raise ValueError(f'{field_name} должен быть str.')

        if not text.strip():
            raise EmptyFieldReviewError(field_name)

        if len(text) > max_length:
            raise IncorrectLengthFieldReviewError(field_name, len(text), max_length)

    def remove_pro(self, index: int) -> None:
        """
        Удаляет плюс из списка плюсов по индексу и проверяет на валидность типа.
        :param index: Индекс удаляемого элемента.
        :raises IndexError: TODO: Описать
        :return: None.
        """
        try:
            del self.__pros[index]
        except IndexError as ex:
            raise IndexError(f"Удаление по некорректному индексу: {index}.") from ex

    def remove_con(self, index: int) -> None:
        """
        Удаляет минус из списка минусов по индексу и проверяет на валидность типа.
        :param index: Индекс удаляемого элемента.
        :raises IndexError: TODO: Описать
        :return: None.
        """
        try:
            del self.__cons[index]
        except IndexError as ex:
            raise IndexError(f"Удаление по некорректному индексу: {index}.") from ex

    @classmethod
    def from_dict(cls, data: ReviewData, base_keys: list[str]) -> Self:
        """
        Создает экземпляр класса из словаря data.
        :param data: Словарь, из которого впоследствии
                мы создаем экземпляр класса Review.
        :param base_keys: Обязательный ключи словаря.
        :raises ValueError: TODO: Описать
        :raises MissingRequiredFieldReviewError: TODO: Описать
        :return: Review.
        """
        if not isinstance(data, dict):
            raise ValueError("data должен быть dict!")

        for key in base_keys:
            if key not in data:
                raise MissingRequiredFieldReviewError(key)

        return cls(
            title=data['title'],
            content=data['content'],
            status=data.get('status', StatusReview.PUBLISHED),
            date=data.get('date'),
            pros=data.get('pros'),
            cons=data.get('cons'),
            author=data.get('author')
            )

    def __repr__(self) -> str:
        """Возвращает отчет об объекте."""
        return (f'Review(title={self.title!r}, content={self.content!r}, status={self.status},'
                f'date={self.date}, pros={self.pros}, cons={self.cons}, author={self.author})')

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return (f'Info review:\n\ttitle={self.title}\n\tcontent={self.content}'
                f'\n\tstatus={self.status}\n\tdate={self.date}'
                f'\n\tpros={self.pros}\n\tcons={self.cons}\n\tauthor={self.author}')