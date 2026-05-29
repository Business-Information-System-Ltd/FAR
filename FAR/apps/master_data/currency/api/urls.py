from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
from apps.master_data.currency.models.currency_models import Currency
from apps.master_data.currency.api.views.currency_views import CurrencyViewSet
router = DefaultRouter()
router.register(r'',CurrencyViewSet)


urlpatterns = [
    path('',include(router.urls)),
<<<<<<< HEAD
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
=======
    
]


>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
