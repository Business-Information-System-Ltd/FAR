<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import viewsets
# Model နဲ့ Serializer ကို folder အပြင်ကနေ လှမ်းခေါ်မယ်
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.branch.api.serializers.branch_serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
=======
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.branch.api.serializers.branch_serializers import BranchSerializer
from rest_framework import viewsets

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774
