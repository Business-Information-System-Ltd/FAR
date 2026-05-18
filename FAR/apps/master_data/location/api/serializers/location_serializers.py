from rest_framework import serializers
from apps.master_data.location.models.location_models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'