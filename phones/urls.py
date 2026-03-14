from django.contrib import admin
from django.urls import path
from .views import phones, details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('phones/<int:phone_id>/', details, name='details'),
    path('phones/', phones, name='phones'),

]

