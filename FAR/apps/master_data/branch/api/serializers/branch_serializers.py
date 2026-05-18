from rest_framework import serializers
from apps.master_data.branch.models.branch_models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'