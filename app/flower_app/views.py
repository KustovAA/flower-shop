from django.shortcuts import render, get_object_or_404
from .models import Bouqet


def index(request):
    return render(request, 'index.html', {})


def catalog(request):
    raw_bouquets = Bouqet.objects.all()
    bouquets = []
    for raw_bouquet in raw_bouquets:
        bouquet = {}
        bouquet['id'] = raw_bouquet.id
        bouquet['title'] = raw_bouquet.title
        bouquet['price'] = int(raw_bouquet.price)
        bouquet['picture'] = raw_bouquet.picture
        bouquets.append(bouquet)
    return render(request, 'catalog.html', context={'bouquets': bouquets})


def consultation(request):
    return render(request, 'consultation.html', {})


def card(request, bouquet_id):
    bouquet = get_object_or_404(Bouqet, id=bouquet_id)
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
