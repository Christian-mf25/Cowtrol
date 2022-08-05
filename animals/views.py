from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from animals.utils import check_animal_name, check_owner_area
from animals.serializers import ListCreateAnimalSerializer
from cowtrol.exceptions import CustomException
from animals.models import Animal
from areas.models import Area


class AnimalView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Animal.objects.all()
    serializer_class = ListCreateAnimalSerializer

    def perform_create(self, serializer):
        animal_name = serializer.data["name"].title()
        animal_weight = serializer.data.get("weight")
        received_area = serializer.data["area"].title()

        area_list = Area.objects.filter(area_name=received_area)
        logged_in_user = self.request.user

        animal_name_list = Animal.objects.filter(name=animal_name)

        area = check_owner_area(area_list, logged_in_user)

        if area.limit_space <= area.occupied_space:
            raise CustomException({"message": "this area is at maximum capacity"}, 409)

        check_animal_name(animal_name_list, logged_in_user)

        Animal.objects.create(
            name=animal_name,
            weight=animal_weight,
            area=area,
            owner_id=logged_in_user.id,
        )

        area_occupied_space = area_list[0].occupied_space + 1
        area_free_space = area_list[0].free_space - 1

        Area.objects.filter(area_name=received_area).update(
            occupied_space=area_occupied_space, free_space=area_free_space
        )
