from django.shortcuts import render
import uuid
from yookassa import Configuration, Payment
from .models import Bouqet,Event,Order,OrderItem
from django.conf import settings
import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect



Configuration.account_id = settings.PAYMENT_ID
Configuration.secret_key = settings.PAYMENT_KEY


def index(request):
    return render(request,'index.html')


def get_bouqet(request, bouqet_id):
    bouqet = get_object_or_404(Bouqet, pk=bouqet_id)
    print(bouqet)
    return HttpResponse(bouqet, content_type="application/json")


def create_payment(request, bouqet_id):
    bouqet = Bouqet.objects.get(pk=bouqet_id)
    payment = Payment.create({
        "amount": {
            "value": bouqet.price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://127.0.0.1:8000"
        },
        "capture": True,
        "description": bouqet.description
    }, uuid.uuid4())
    print(payment.json())
    print(payment.confirmation.confirmation_url)
    # return HttpResponse({'payments':payment.json()})
    return redirect(payment.confirmation.confirmation_url)
    #return HttpResponse(payment.json(), content_type="application/json")


def get_payment(request):
    # Configuration.account_id = settings.PAYMENT_ID
    # Configuration.secret_key = settings.PAYMENT_KEY
    payment = Payment.find_one("2b5ca2b0-000f-5000-8000-116ecab21e00")
    return HttpResponse(payment.json(),content_type="application/json")

# Create your views here.
