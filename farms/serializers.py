from cowtrol.exceptions import CustomException
from rest_framework import serializers
from django.db import IntegrityError
from farms.models import Farm

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm

        fields = ("id", "name", "email", "password")

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        try:
            validated_data["email"] = validated_data["email"].lower()
            validated_data["name"] = validated_data["name"].title()
            return Farm.objects.create_user(**validated_data)

        except IntegrityError:
            raise CustomException("E-mail already exists", 422)