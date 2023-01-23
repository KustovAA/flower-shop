from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flower_app.urls')),
    path('order/', include('payment_app.urls')),
]
