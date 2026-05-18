
from rest_framework import serializers
from apps.master_data.custodian.models.custodian_models import Custodian

class CustodianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custodian
        fields = '__all__'