from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from areas.serializers import ListCreateAreaSerializer
from cowtrol.exceptions import CustomException
from areas.models import Area


class AreaView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Area.objects.all()
    serializer_class = ListCreateAreaSerializer

    def perform_create(self, serializer):
        serializer.save(farm=self.request.user)

    def post(self, request, *args, **kwargs):
        areas_list = Area.objects.filter(farm_id=request.user.id)
        received_data = request.data

        for item in areas_list:
            if received_data["area_name"].title() == item.area_name:
                raise CustomException(
                    {"message":"area_name already exists"}, 
                    422
                )

        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.queryset = Area.objects.filter(farm_id=request.user.id)
        return super().get(request, *args, **kwargs)
