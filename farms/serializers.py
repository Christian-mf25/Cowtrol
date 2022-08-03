from rest_framework import serializers
from farms.models import Farm

class FarmSerializer(serializers.ModelSerializer):
	class Meta:
		model = Farm

		fields = ("id", "name",)

		extra_kwargs = {
			"id": {"read_only": True},
			"password": {"write_only": True},
		}

	def create(self, validated_data):
		print(validated_data)
		return  Farm.objects.create_user(**validated_data)