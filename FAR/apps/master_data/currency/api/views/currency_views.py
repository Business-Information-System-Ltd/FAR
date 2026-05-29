
<<<<<<< HEAD
from apps.master_data.currency.models.currency_models import Currency
from apps.master_data.currency.api.serializers.currency_serializers import CurrencySerializer
from rest_framework import viewsets

=======
from rest_framework import viewsets
from apps.master_data.currency.models import Currency
from apps.master_data.currency.api.serializers.currency_serializers import CurrencySerializer
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer