from django.db import models

<<<<<<< HEAD
class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)

    currency_code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=50)
    currency_symbol = models.CharField(max_length=10, null=True, blank=True)

    decimal_places = models.IntegerField(default=2)

=======

class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency_code = models.CharField(max_length=3,null =False)
    currency_name = models.CharField(max_length=50,null = False)
    currency_symbol = models.CharField(max_length=10)
    decimal_places = models.IntegerField(default=2)
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
    is_functional_currency = models.BooleanField(default=False)
    is_presentation_currency = models.BooleanField(default=False)
    allow_transaction_currency = models.BooleanField(default=True)
    allow_exchange_rate_entry = models.BooleanField(default=True)
<<<<<<< HEAD


    amount_rounding_precision = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.01
    )
    depreciation_rounding = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.01
    )

    transaction_currency = models.CharField(max_length=3, null=True, blank=True)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
    functional_currency = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "currency"

    def __str__(self):
        return self.currency_code

=======
    amount_rounding_precision = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    depreciation_rounding = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    transaction_currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
    functional_currency = models.DecimalField(max_digits=20, decimal_places=6)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    class Meta:
        db_table = 'currency'

    def __str__(self):
        return self.currency_name
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
