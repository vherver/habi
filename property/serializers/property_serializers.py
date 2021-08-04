from rest_framework import serializers

from property.models import Property


class PropertySerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_name")

    class Meta:
        model = Property
        fields = "__all__"
