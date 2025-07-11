import random

from django.core.management import BaseCommand
from django.db import transaction

from core.choices import QualityChoices
from core.models import Guest, Product, Member, SocialClub
import requests


def _get_random_first_last(results: int):
    response = requests.get(
        f"https://randomuser.me/api/?results={results}&seed={results}"
    )
    response.raise_for_status()
    data = [
        (data["name"]["first"], data["name"]["last"])
        for data in response.json()["results"]
    ]
    return data


product_names = [
    "Marsh Wintercress",
    "Eagle Poisonberry",
    "Whisper Laceflower",
    "Deadly Hemp",
    "Thrade",
    "Anon",
    "Eoknedgoil",
    "Brukmite",
    "Silver Inkberry",
    "Dragon Groundberry",
    "Fatigue Joy",
    "Vision Shadblow",
    "Glacier Grass",
    "Ifyegon",
    "Itium",
    "Asriffoss",
    "Odrastine",
    "Adasliscus",
]

MEMBER_COUNT = 122
GUEST_COUNT = 55


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        clubs = [
            SocialClub.objects.create(
                name=f"Social Club No. {i}",
                street=f"Social Street {i}",
                zip=random.randint(11111, 99999),
            )
            for i in range(10)
        ]
        member_data = _get_random_first_last(MEMBER_COUNT)
        for i in range(MEMBER_COUNT):
            first_name, last_name = member_data[i]
            Member.objects.create(
                first_name=first_name,
                last_name=last_name,
                social_club=random.choices(clubs)[0],
                age=random.randint(0, 50),
            )
        guest_data = _get_random_first_last(GUEST_COUNT)
        for i in range(GUEST_COUNT):
            first_name, last_name = guest_data[i]
            Guest.objects.create(
                first_name=first_name,
                last_name=last_name,
                social_club=random.choices(clubs)[0],
                rating=random.randint(0, 5),
            )
        for name in product_names:
            qualities = [k for (k, _) in QualityChoices.choices]
            Product.objects.create(
                name=name,
                quality=random.choices(qualities)[0],
                price=random.randint(3, 15),
                social_club=random.choices(clubs)[0],
            )
