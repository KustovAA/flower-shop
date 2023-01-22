import random
from django.shortcuts import render
from .models import Bouqet


def index(request):
    return render(request, 'index.html', {})


def catalog(request):
    return render(request, 'catalog.html', {})


def consultation(request):
    return render(request, 'consultation.html', {})


def card(request):
    return render(request, 'card.html', {})


def order(request):
    return render(request, 'order.html', {})


def order_step(request):
    return render(request, 'order-step.html', {})


def quiz(request):
    return render(request, 'quiz.html', {})


def quiz_step(request):
    event = request.GET.get('event', '')
    return render(request, 'quiz-step.html', {'event': event})


def result(request):
    event = request.GET.get('event', '')
    budget = request.GET.get('budget', '')
    price = ({
      'small': 1000,
      'medium': 5000,
    }).get(budget, 1000000)

    bouquets = Bouqet.objects.filter(price__lte=price)
    if len(bouquets) == 0:
        bouquets = Bouqet.objects.all()

    bouquet = random.choice(bouquets)

    return render(request, 'result.html', {'bouquet': bouquet})
