from rest_framework import serializers
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.country.models.country_models import Country


class BranchSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source = 'country.country_name', read_only=True)
    class Meta:
        model = Branch
        fields = '__all__'