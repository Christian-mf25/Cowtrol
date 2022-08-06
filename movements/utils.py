from django.shortcuts import get_object_or_404
from django.http import Http404

from cowtrol.exceptions import CustomException
from animals.models import Animal
from areas.models import Area


def check_animals_name_exist(serializer, name_list, farm):
    try:
        found_animals = []

        for item in name_list:
            animal = get_object_or_404(Animal, name__icontains=item.title())
            if str(animal.owner_id) != str(farm.id):
                raise Http404

            if animal in found_animals:
                raise CustomException(
                    {"message": f"animal '{animal.name}' is repeated in the list"},
                    409
                )

            found_animals.append(animal)

        return found_animals

    except Http404:
        right_names_length = len(found_animals)
        wrong_name = serializer.data["animals"][right_names_length]

        raise CustomException(
            {"message": f"animal '{wrong_name}' not found"},
            404
        )


def check_area_exists(area, farm):
    found_area = Area.objects.filter(area_name=area)
    move_to_area = []

    for item in found_area:
        if item.farm.id == farm.id:
            move_to_area.append(item.area_name)
            return item

    if not move_to_area:
        raise CustomException(
            {"message": "area not found"},
            404
        )


def check_move_area(animals, area):
    for item in animals:
        if item.area.id == area.id:
            raise CustomException(
                {"message": f"animal '{item.name}' is already in area '{area.area_name}'"},
                409,
            )


def check_enough_free_space(area, animals):
    if area.free_space < len(animals):
        raise CustomException(
            {"message": f"not enough space in '{area.area_name}' for this movement"},
            409,
        )
