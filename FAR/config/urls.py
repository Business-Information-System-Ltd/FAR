

from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from apps.master_data.branch.meta.branch_field_meta_view import BranchFieldMetaView
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/far/meta/currencies/fields/',
         #BranchFieldMetaView.as_view(),name='currency_meta'),

    path('api/far/meta/', include([
        path('branches/', include('apps.master_data.branch.api.urls')),
        path('countries/', include('apps.master_data.country.api.urls')),
        path('currencies/', include('apps.master_data.currency.api.urls')),
        path('locations/', include('apps.master_data.location.api.urls')),
        path('custodians/', include('apps.master_data.custodian.api.urls')),
        path('departments/', include('apps.master_data.department.api.urls')),
        

])),
]
