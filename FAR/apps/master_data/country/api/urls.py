from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD

from apps.master_data.country.api.views.country_views import CountryViewSet
from apps.master_data.country.models.country_models import Country



router = DefaultRouter()
router.register(r'', CountryViewSet)

urlpatterns = [
     path('', include(router.urls)),
    

=======
from apps.master_data.country.models.country_models import Country
from apps.master_data.country.api.views.country_views import CountryViewSet
from apps.master_data.country.meta.country_field_meta_view import CountryFieldMetaView

from.serializers import*
router = DefaultRouter()
router.register(r'',CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "fields/<str:field_name>/",
        CountryFieldMetaView.as_view()
    ),

>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
]
