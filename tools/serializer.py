from rest_framework import serializers
from .models import Tool


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "user",
            "price",
            "description",
            "number_in_inventory",
            "last_updated",
        )
        model = Tool