from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from apps.master_data.location.models.location_models import Location
from apps.master_data.location.api.serializers.location_serializers import LocationSerializer
from apps.common.utils.search.search_engine import SearchEngine

class LocationViewSet(viewsets.ModelViewSet):  
    queryset = Location.objects.select_related('parent_location', 'country').all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username if self.request.user.is_authenticated else "System")


    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username if self.request.user.is_authenticated else "System")


class LocationView(APIView):

    def get(self, request):

        search = request.GET.get("search")

        queryset = Location.objects.all()

        if search:
            q = SearchEngine.parse(search, "location")

            print("RAW SEARCH:", search)
            print("PARSED Q:", q)
            print("Q CHILDREN:", q.children)

            # 🔥 FORCE DEBUG RESULT
            if not q.children:
                print("❌ EMPTY Q - NO FILTER APPLIED")
                return Response([])

            queryset = queryset.filter(q)

        print("FINAL SQL:", queryset.query)

        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    