import json
from flower_app.models import Bouqet


def save_bouquet(raw_bouquet):
    bouquet, created = Bouqet.objects.get_or_create(
        title=raw_bouquet.get('title'),
        price=raw_bouquet.get('price'),
        flowers=raw_bouquet.get('flowers'),
        size=raw_bouquet.get('size'),
        description=raw_bouquet.get('description'),
        picture=raw_bouquet.get('link')
    )


def main():
    with open('bouquets.json', 'r') as file:
        bouquets = json.loads(file.read())

    for bouquet in bouquets:
        save_bouquet(bouquet)


if __name__ == '__main__':
    main()
