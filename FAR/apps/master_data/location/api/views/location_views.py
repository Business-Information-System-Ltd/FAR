from rest_framework import viewsets
from apps.master_data.location.models.location_models import Location
from apps.master_data.location.api.serializers.location_serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):  
    queryset = Location.objects.all()
    serializer_class = LocationSerializer