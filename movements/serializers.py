from rest_framework import serializers

from movements.models import Movement


class CreateMovementSerializer(serializers.ModelSerializer):
    animals = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Movement

        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
            "move_from": {"read_only": True},
            "start_date": {"read_only": True},
            "end_date": {"read_only": True},
        }
