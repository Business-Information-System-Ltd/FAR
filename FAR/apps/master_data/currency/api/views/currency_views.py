<<<<<<< HEAD

from rest_framework import viewsets
from apps.master_data.currency.models import Currency
from apps.master_data.currency.api.serializers.currency_serializers import CurrencySerializer
=======
from apps.master_data.currency.models.currency_models import Currency
from apps.master_data.currency.api.serializers.currency_serializers import CurrencySerializer
from rest_framework import viewsets
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer