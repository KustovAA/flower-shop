import json

from django.core.management.base import BaseCommand
from flower_app.models import Bouqet


class Command(BaseCommand):
    help = 'Populate DB with data'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='File path')

    def handle(self, *args, **kwargs):
        file = kwargs.get('file')
        with open(file, 'r') as file:
            raw_bouquets = json.loads(file.read())

        for raw_bouquet in raw_bouquets:
            bouquet, created = Bouqet.objects.get_or_create(
                title=raw_bouquet.get('title'),
                price=raw_bouquet.get('price'),
                flowers=raw_bouquet.get('flowers'),
                size=raw_bouquet.get('size'),
                description=raw_bouquet.get('description'),
                picture=raw_bouquet.get('link')
            )
        print('Данные успешно добавлены')
