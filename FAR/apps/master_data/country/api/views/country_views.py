from django.shortcuts import render
from apps.master_data.country.models.country_models import *
from rest_framework import viewsets
from apps.master_data.country.api.serializers.country_serializers import CountrySerializer 
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
# Create your views here.

