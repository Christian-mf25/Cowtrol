from rest_framework import serializers

from animals.models import Animal
from areas.serializers import ListAreaSerializer


class CreateAnimalSerializer(serializers.ModelSerializer):
    area = serializers.CharField()

    class Meta:
        model = Animal

        fields = [
            "name",
            "weight",
            "area",
        ]


class ListAnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    weight = serializers.CharField()
    area = ListAreaSerializer()
