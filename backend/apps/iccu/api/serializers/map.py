from rest_framework import serializers

from ...models import Complex, Place

__all__ = (
    "PlaceSerializer",
    "ComplexSerializer",
)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "name", "full_name", "icon", "link", "latitude", "longitude"]


class ComplexSerializer(serializers.ModelSerializer):
    places = serializers.SerializerMethodField()

    class Meta:
        model = Complex
        fields = ["id", "title", "orienteer", "places"]

    def get_places(self, obj):
        active_places = obj.places.filter(is_active=True)
        return PlaceSerializer(active_places, many=True, context=self.context).data
