from django.shortcuts import render, redirect
from yookassa import Configuration, Payment
from flower_app.models import Bouqet,Event,Order,OrderItem
from django.conf import settings
import uuid
from django.shortcuts import get_object_or_404
from django.urls import reverse


Configuration.account_id = settings.PAYMENT_ID
Configuration.secret_key = settings.PAYMENT_KEY


def create_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    payment = Payment.create({
        "amount": {
            "value": order.get_total_cost(),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"http://127.0.0.1:8000/order/success_payment/{order_id}"
        },
        "capture": True,
        "description": f'Номер вашего заказа {order.pk}',
    }, uuid.uuid4())
    if payment:
        order.status = 'UNPROCESSED'
        order.payment_id = payment.id
        order.save()
    return redirect(payment.confirmation.confirmation_url)


def payment_completed(request, order_id):
    order = Order.objects.get(pk=order_id)
    payment = Payment.find_one(order.payment_id)
    if payment.paid:
        order.status = 'SUCCESS'
        order.save()
    return redirect(reverse('flower_app:index'))


# Create your views here.
