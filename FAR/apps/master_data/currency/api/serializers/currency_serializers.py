<<<<<<< HEAD

from rest_framework import serializers 
# from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.currency.models.currency_models import Currency

=======
from rest_framework import serializers
from apps.master_data.currency.models import Currency
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
<<<<<<< HEAD

        fields = "__all__"

=======
        fields = '__all__'
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
