from rest_framework import serializers

from ...models import Banner, Schedule

__all__ = ("PlaceBannerSerializer",)


class PlaceBannerSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    is_open_now = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = [
            "id",
            "name",
            "short_name",
            "image_url",
            "city",
            "country",
            "location",
            "is_open_now",
            "status_display",
        ]

    def get_location(self, obj):
        return f"{obj.city}, {obj.country}"

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url if obj.image else None

    def get_is_open_now(self, obj):
        day = Schedule.today()
        return day.is_open_now if day else False

    def get_status_display(self, obj):
        day = Schedule.today()
        return str(day.status_display) if day else ""

    def get_today_schedule(self, obj):
        day = Schedule.today()
        return day.hours_display if day else None
