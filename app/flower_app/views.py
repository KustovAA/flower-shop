from django.shortcuts import render
import uuid
from yookassa import Configuration, Payment
from .models import Bouqet,Event,Order,OrderItem
from django.conf import settings
import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect



def index(request):
    return render(request, 'index.html')









