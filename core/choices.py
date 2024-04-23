from django.db import models


class QualityChoices(models.IntegerChoices):
    BAD = 1, "Bad"
    OK = 2, "OK"
    GOOD = 3, "Good"
