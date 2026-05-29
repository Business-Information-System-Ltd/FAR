<<<<<<< HEAD

from rest_framework import serializers 
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.country.models.country_models import Country



class BranchSerializer(serializers.ModelSerializer): 
    

=======
from rest_framework import serializers
from apps.master_data.branch.models.branch_models import Branch
<<<<<<< HEAD
import apps.common.validators.validators

class BranchSerializer(serializers.ModelSerializer):
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
=======
from apps.master_data.country.models.country_models import Country


class BranchSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source = 'country.country_name', read_only=True)
>>>>>>> 5bedb4fc78dd79be22858d46885bd0e4d45a6d72
    class Meta:
        model = Branch
        fields = "__all__"

   
    def validate_branch_code(self, value):
        return validate_branch_code_format(value)

    
<<<<<<< HEAD

=======
    def validate_branch_name(self, value):
        return validate_branch_name_required(value)
>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
