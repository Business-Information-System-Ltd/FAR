from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.master_data.currency.models.currency_models import Currency
from apps.master_data.currency.api.views.currency_views import CurrencyViewSet
router = DefaultRouter()
router.register(r'',CurrencyViewSet)


urlpatterns = [
    path('',include(router.urls)),
    
]


