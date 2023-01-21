from django.urls import path,include
from . import views


app_name = 'flower_app'

urlpatterns = [
    path('', views.index, name='main'),
#    path('bouqet/<int:bouqet_id>/', views.get_bouqet, name='bouqet'),
    #path('payment/<int:bouqet_id>/', views.create_payment, name='payments'),
#    path('success_payment/', views.done),

]
