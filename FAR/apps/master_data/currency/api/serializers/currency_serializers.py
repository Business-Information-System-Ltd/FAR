
from rest_framework import serializers 
# from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.currency.models.currency_models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency

        fields = "__all__"

