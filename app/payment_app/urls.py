from django.urls import path,include
from . import views


app_name = 'payment_app'

urlpatterns = [
    path('payment/<int:order_id>/', views.create_payment, name='youkassa_payment'),
    path('success_payment/<int:order_id>/', views.payment_completed,name='payment_done' ),

]