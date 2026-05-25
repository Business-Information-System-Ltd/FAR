from django.db import models
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.department.models.department_models import Department






class Custodian(models.Model):
    custodian_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, db_column='branch_id')
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_id')
    custodian_code = models.CharField(max_length=10)
    custodian_name = models.CharField(max_length=100,null = False)
    custodian_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    can_hold_assets = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    class Meta:
        db_table = 'custodian'

    def __str__(self):
        return self.custodian_name