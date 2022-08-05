from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from animals.serializers import CreateAnimalSerializer, ListAnimalSerializer
from animals.utils import check_animal_name, check_owner_area
from cowtrol.exceptions import CustomException
from animals.models import Animal
from areas.models import Area


class AnimalView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Animal.objects.all()
    serializer_class = CreateAnimalSerializer

    def list(self, request, *args, **kwargs):
        farm_id = request.user.id

        self.serializer_class = ListAnimalSerializer
        self.queryset = Animal.objects.filter(owner_id=farm_id)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        animal_name = serializer.data["name"].title()
        animal_weight = serializer.data.get("weight")
        received_area = serializer.data["area"].title()

        animal_name_list = Animal.objects.filter(name=animal_name)
        area_list = Area.objects.filter(area_name=received_area)
        farm = self.request.user

        area = check_owner_area(area_list, farm)

        if area.limit_space <= area.occupied_space:
            raise CustomException(
				{"message": "this area is at maximum capacity"}, 
				409
			)

        check_animal_name(animal_name_list, farm)

        Animal.objects.create(
            name=animal_name,
            weight=animal_weight,
            area=area,
            owner_id=farm.id,
        )

        area_occupied_space = area_list[0].occupied_space + 1
        area_free_space = area_list[0].free_space - 1

        Area.objects.filter(area_name=received_area).update(
            occupied_space=area_occupied_space, free_space=area_free_space
        )
