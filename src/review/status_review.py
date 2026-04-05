from enum import StrEnum

class StatusReview(StrEnum):
    """Инициализирует статус обзора."""
    PUBLISHED = "published"
    ARCHIVED = "archived"
    DRAFT = "draft"


