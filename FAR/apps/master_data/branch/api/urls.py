from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD

from apps.master_data.branch.api.views.branch_views import BranchViewSet
from apps.master_data.branch.models.branch_models import Branch


router = DefaultRouter()
router.register(r'', BranchViewSet)

urlpatterns = [
     path('', include(router.urls)),
     
    

=======
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.branch.api.views.branch_views import BranchViewSet
from apps.master_data.branch.meta.branch_field_meta_view import BranchFieldMetaView

router = DefaultRouter()
router.register(r'',BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "fields/<str:field_name>/",
        BranchFieldMetaView.as_view()
    ),

>>>>>>> c45243217a8bad0bf81b22554dcaf8f8649bfa16
]
