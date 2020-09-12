from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from . import viewsets


clicksign_router = routers.DefaultRouter()
clicksign_router.register(r'confirmation', viewsets.ConfirmationViewSet, base_name='clicksign_confirmation')
clicksign_router.register(r'signature', viewsets.SignatureViewSet, base_name='clicksign_signature')


urlpatterns = [
    path('', include(clicksign_router.urls)),
]
