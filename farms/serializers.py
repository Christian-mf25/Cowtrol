from rest_framework import serializers
from django.db import IntegrityError
from farms.models import Farm

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm

        # fields = ("id", "email", "name",)
        fields = ("id", "name", "email", "password")

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        try:
            farm: Farm = self.context["request"].user
            print("A"*1000)
            print(farm)
            # user: Farm = self.context["request"].user
            validated_data["email"] = validated_data["email"].lower()
            validated_data["name"] = validated_data["name"].title()
            # print("A"*1000)
            return Farm.objects.create_user(**validated_data)

        except:
            return "Teste"