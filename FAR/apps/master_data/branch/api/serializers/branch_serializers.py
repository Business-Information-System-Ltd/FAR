from rest_framework import serializers
from apps.master_data.branch.models.branch_models import Branch
import apps.common.validators.validators

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

   
    def validate_branch_code(self, value):
        return validate_branch_code_format(value)

    
    def validate_branch_name(self, value):
        return validate_branch_name_required(value)