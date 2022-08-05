from rest_framework import serializers

from animals.models import Animal


class ListCreateAnimalSerializer(serializers.ModelSerializer):
    area = serializers.CharField()

    class Meta:
        model = Animal

        fields = [
            "name",
            "weight",
            "area",
        ]
