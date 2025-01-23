from django.core.management import BaseCommand

from core.utils import RedisSingleTone


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'message',
            nargs='?',
            default='Hello from Django!',
            help='The message to display'
        )

    def handle(self, *args, **options):
        message = options['message']
        RedisSingleTone.publish('message', message)
