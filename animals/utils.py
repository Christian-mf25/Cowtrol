from django.shortcuts import get_object_or_404
from cowtrol.exceptions import CustomException
from areas.models import Area


def check_owner_area(area_list, user):
    found_area = []
    for item in area_list:
        if item.farm == user:
            found_area.append(get_object_or_404(Area, id__icontains=item.id))

            return found_area[0]

    raise CustomException(
		{"message": "area not found"},
		404
	)


def check_animal_name(animal_list, user):
    for item in animal_list:
        animal_owner_id = str(item.owner_id)
        user_id = str(user.id)

        if animal_owner_id == user_id:
            raise CustomException(
				{"message": "name already exists"},
				422
			)
