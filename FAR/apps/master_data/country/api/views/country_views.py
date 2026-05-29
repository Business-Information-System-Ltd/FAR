<<<<<<< HEAD

from apps.master_data.country.models.country_models import Country
from apps.master_data.country.api.serializers.country_serializers import CountrySerializer
from rest_framework import viewsets

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

=======
from django.shortcuts import render
from apps.master_data.country.models.country_models import *
from rest_framework import viewsets
from apps.master_data.country.api.serializers.country_serializers import CountrySerializer 
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
# Create your views here.
 
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
