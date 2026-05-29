from rest_framework import serializers
from apps.master_data.location.models.location_models import Location

class LocationSerializer(serializers.ModelSerializer):

    full_path = serializers.SerializerMethodField()
    full_location_code = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = '__all__'

    def get_full_path(self, obj):
        if obj.parent_location:
            return f"{self.get_full_path(obj.parent_location)} >> {obj.location_name}"
        return obj.location_name
    
    def get_full_location_code(self, obj):
        current_code = obj.location_code if obj.location_code else ""
        
        if obj.parent_location:
            parent_code_path = self.get_full_location_code(obj.parent_location)
            return f"{parent_code_path}-{current_code}" if parent_code_path and current_code else parent_code_path or current_code
            
        return current_code