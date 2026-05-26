<<<<<<< HEAD
from rest_framework import serializers
from apps.master_data.branch.models.branch_models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
=======
from rest_framework import serializers 
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.country.models.country_models import Country



class BranchSerializer(serializers.ModelSerializer): 
    

    class Meta:
        model = Branch
        fields = "__all__"

    
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774
