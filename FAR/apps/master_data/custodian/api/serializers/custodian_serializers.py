
from rest_framework import serializers
from apps.master_data.custodian.models.custodian_models import Custodian

class CustodianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custodian
        fields = '__all__'
        dept = 1
        extra_kwargs = {
            'created_by': {'read_only': True},  
            'updated_by': {'read_only': True},  
        }
        