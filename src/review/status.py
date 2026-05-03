from enum import StrEnum


class StatusReview(StrEnum):
    """Инициализирует статус обзора."""

    PUBLISHED = "published"
    ARCHIVED = "archived"
    DRAFT = "draft"

    @staticmethod
    def to_list() -> list[str]:
        """Возвращает значения StatusReview."""
        return [i.value for i in StatusReview]
