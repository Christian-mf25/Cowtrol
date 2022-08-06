from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404

from cowtrol.exceptions import CustomException
from animals.models import Animal
from areas.models import Area


def check_owner_area(area_list, farm):
    found_area = []
    for item in area_list:
        if item.farm == farm:
            found_area.append(get_object_or_404(Area, id=item.id))

            return found_area[0]

    raise CustomException({"message": "area not found"}, 404)


def check_animal_name(animal_list, farm):
    for item in animal_list:
        animal_owner_id = str(item.owner_id)
        farm_id = str(farm.id)

        if animal_owner_id == farm_id:
            raise CustomException({"message": "name already exists"}, 422)


def validate_json_key_name(request):
    if "animal_names" not in request.data:
        raise CustomException(
            {"message": "the only field allowed is 'animal_names'"}, 400
        )


def validate_retrieve_string_type(animal_names, farm_id):
    try:
        found_animals = get_list_or_404(Animal, name=animal_names.title())
        animal_list = [
            item.id for item in found_animals if str(item.owner_id) == str(farm_id)
        ]
        
        if not animal_list:
            raise Http404

        return animal_list

    except Http404:
        raise CustomException({"message": "animal not found"}, 404)


def validate_retrieve_list_type(animal_names, farm_id):
    try:
        animal_list = []
        duplicate_animal = []

        for item in animal_names:
            filter_animal = get_list_or_404(Animal, name=item.title())

            for animal in filter_animal:
                if str(animal.owner_id) == str(farm_id):
                    animal_list.append(animal.id)
                

        for item in animal_list:
            if item not in duplicate_animal:
                duplicate_animal.append(item)

            else:
                animal = Animal.objects.filter(id=item)[0]
                raise CustomException(
                    {"message": f"animal '{animal.name}' is repeated in the list"},
                    409,
                )
        return animal_list

    except Http404:
        right_names_length = len(animal_list)
        wrong_name = animal_names[right_names_length]
        raise CustomException({"message": f"animal '{wrong_name}' not found"}, 404)
