from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta
from rest_framework import generics
from areas.models import Area


from movements.utils import (
    check_animals_name_exist,
    check_area_exists,
    check_enough_free_space,
    check_move_area,
)
from movements.serializers import CreateMovementSerializer
from cowtrol.exceptions import CustomException
from movements.models import Movement
from animals.models import Animal


class MovementView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Movement.objects.all()
    serializer_class = CreateMovementSerializer

    def perform_create(self, serializer):
        move_to_area = serializer.data["move_to"].title()
        animals_list_name = serializer.data["animals"]
        time = serializer.data["days"]
        farm = self.request.user

        animals = check_animals_name_exist(serializer, animals_list_name, farm)

        area = check_area_exists(move_to_area, farm)

        check_move_area(animals, area)
        check_enough_free_space(area, animals)

        present_day = date.today()
        sum_days = present_day + timedelta(days=time)

        move_from = animals[0].area
        total_gain = time * area.gmd

        movement = Movement.objects.create(
            move_from=move_from.area_name,
            move_to=serializer.data["move_to"],
            days=serializer.data["days"],
            end_date=sum_days,
        )
        movement.animals.set(animals)

        for item in animals:
            Animal.objects.filter(name=item.name).update(
                area=area,
                weight=item.weight + total_gain,
            )

        Area.objects.filter(id=area.id).update(
            free_space=area.free_space - len(animals),
            occupied_space=area.occupied_space + len(animals),
        )

        Area.objects.filter(id=move_from.id).update(
            free_space=move_from.free_space + len(animals),
            occupied_space=move_from.occupied_space - len(animals),
        )

    def get(self, request, *args, **kwargs):
        raise CustomException({"message": "method in development"}, 405)
