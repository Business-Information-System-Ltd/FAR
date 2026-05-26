from django.db import models
<<<<<<< HEAD
from apps.master_data.country.models.country_models import Country

class Branch(models.Model):
    
    branch_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        related_name='branches'
    )
    
    branch_code = models.CharField(max_length=10, null=True, blank=True)
    branch_name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Audit tracking
=======


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)

    country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        db_column="country_id"
    )

    branch_code = models.CharField(max_length=10, null=True, blank=True)
    branch_name = models.CharField(max_length=100)

    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    postal_code = models.IntegerField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
<<<<<<< HEAD
        db_table = 'branch'  # Ensures the table name matches your SQL exactly
=======
        db_table = "branch"
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774

    def __str__(self):
        return self.branch_name