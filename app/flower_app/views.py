from django.shortcuts import render, get_object_or_404
from .models import Bouqet
from more_itertools import chunked


def index(request):
    return render(request, 'index.html', {})


def catalog(request):
    bouquets = Bouqet.objects.values_list()
    bouquets_parts = list(chunked(bouquets, 3))
    picture_one = 'https://i.ibb.co/2sRS8z2/image.jpg'
    return render(request, 'catalog.html', context={
        'bouquets': bouquets_parts, 'picture_one': picture_one
    })


def consultation(request):
    return render(request, 'consultation.html', {})


def card(request, bouquet_id):
    bouquet = get_object_or_404(Bouqet, id=bouquet_id)
    print(type(bouquet.flowers))
    selected_bouquet = {
        'title': bouquet.title,
        'price': int(bouquet.price),
        'flowers': [flower.strip() for flower in bouquet.flowers.split(',')],
        'size': [side.strip() for side in bouquet.size.split(' ')],
        'picture': bouquet.picture,
    }
    return render(request, 'card.html', context={'bouquet': selected_bouquet})


def order(request):
    return render(request, 'order.html', {})


def order_step(request):
    return render(request, 'order-step.html', {})


def quiz(request):
    return render(request, 'quiz.html', {})


def quiz_step(request):
    return render(request, 'quiz-step.html', {})


def result(request):
    return render(request, 'result.html', {})
