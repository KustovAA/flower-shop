from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('consultation', views.consultation, name='consultation'),
    path('card', views.card, name='card'),
    path('order', views.order, name='order'),
    path('order-test', views.order, name='order-test'),
    path('order-step', views.order_step, name='order-step'),
    path('quiz', views.quiz, name='quiz'),
    path('quiz-step', views.quiz_step, name='quiz-step'),
    path('result', views.result, name='result'),
]
