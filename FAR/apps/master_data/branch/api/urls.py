from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.branch.api.views.branch_views import BranchViewSet

router = DefaultRouter()
router.register(r'',BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
=======
from apps.master_data.branch.api.views.branch_views import BranchViewSet
from apps.master_data.branch.models.branch_models import Branch


router = DefaultRouter()
router.register(r'', BranchViewSet)

urlpatterns = [
     path('', include(router.urls)),
     
    
>>>>>>> 2e4202d6465e010ac92d5bd480173c8091e90774
]
