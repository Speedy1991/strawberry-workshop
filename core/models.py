from django.db import models

from core.choices import QualityChoices
from core.utils import RedisSingleTone


class SocialClub(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        RedisSingleTone.publish('social_club_create_update', self.id)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    social_club = models.ForeignKey(SocialClub, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    quality = models.PositiveSmallIntegerField(choices=QualityChoices.choices, default=QualityChoices.GOOD)

    def __str__(self):
        return f'{self.name} {self.quality} {self.price}'


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    social_club = models.ForeignKey(SocialClub, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} [{self.social_club}]'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        RedisSingleTone.publish('social_club_create_update', self.social_club_id)


    class Meta:
        abstract = True
        unique_together = (('first_name', 'last_name'),)


class Member(Person):
    age = models.PositiveSmallIntegerField(default=0)


class Guest(Person):
    rating = models.PositiveSmallIntegerField(default=0)
