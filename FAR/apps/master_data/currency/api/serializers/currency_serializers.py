<<<<<<< HEAD
from rest_framework import serializers
from apps.master_data.currency.models import Currency
=======
from rest_framework import serializers 
# from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.currency.models.currency_models import Currency
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774
