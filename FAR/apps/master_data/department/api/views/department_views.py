from rest_framework import viewsets
from apps.master_data.department.models import Department
from apps.master_data.department.api.serializers.department_serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer