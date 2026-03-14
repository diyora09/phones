from django.contrib import admin
from django.urls import path
from .views import phones, details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:phone_id>/', details, name='details'),
    path('', phones, name='phones'),
]

