from rest_framework import serializers

from areas.models import Area


class ListCreateAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area

        fields = [
            "id",
            "area_name",
            "limit_space",
            "free_space",
            "occupied_space",
            "gmd",
]

        extra_kwargs = {
            "id": {"read_only": True},
            "free_space": {"read_only": True},
            "occupied_space": {"read_only": True},
        }

    def validate(self, attrs):
        attrs["free_space"] = attrs["limit_space"]
        return super().validate(attrs)
