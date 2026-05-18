
from rest_framework import viewsets
from apps.master_data.currency.models import Currency
from apps.master_data.currency.api.serializers.currency_serializers import CurrencySerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer