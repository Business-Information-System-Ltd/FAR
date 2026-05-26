from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from apps.master_data.currency.models.currency_models import Currency
from apps.master_data.currency.api.views.currency_views import CurrencyViewSet
router = DefaultRouter()
router.register(r'',CurrencyViewSet)


urlpatterns = [
    path('',include(router.urls)),
]

=======
from apps.master_data.currency.api.views.currency_views import CurrencyViewSet
from apps.master_data.currency.models.currency_models import Currency



router = DefaultRouter()
router.register(r'', CurrencyViewSet)

urlpatterns = [
     path('', include(router.urls)),
    
]
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774
