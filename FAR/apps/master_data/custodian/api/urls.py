from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.master_data.custodian.models.custodian_models import Custodian
from apps.master_data.custodian.api.views.custodian_views import CustodianViewSet
from .serializers import *
router = DefaultRouter()
router.register(r'',CustodianViewSet)


urlpatterns = [
    path('',include(router.urls)),
]

