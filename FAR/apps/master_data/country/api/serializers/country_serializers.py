from rest_framework import serializers
from apps.master_data.country.models.country_models import Country
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
