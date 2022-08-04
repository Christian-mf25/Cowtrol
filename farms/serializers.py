from rest_framework import serializers
from django.db import IntegrityError

from cowtrol.exceptions import CustomException
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
            raise CustomException({"message": "E-mail already exists"}, 422)

class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField(required=True)
	password = serializers.CharField(write_only=True, required=True)