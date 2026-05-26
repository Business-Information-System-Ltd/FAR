from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from apps.master_data.country.models.country_models import Country
from apps.master_data.country.api.views.country_views import CountryViewSet


from.serializers import*
router = DefaultRouter()
router.register(r'',CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
=======
from apps.master_data.country.api.views.country_views import CountryViewSet
from apps.master_data.country.models.country_models import Country



router = DefaultRouter()
router.register(r'', CountryViewSet)

urlpatterns = [
     path('', include(router.urls)),
    
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774
]
