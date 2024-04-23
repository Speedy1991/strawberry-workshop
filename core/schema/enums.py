import strawberry

from core.choices import QualityChoices

QualityEnum = strawberry.enum(QualityChoices, name='QualityEnum')
