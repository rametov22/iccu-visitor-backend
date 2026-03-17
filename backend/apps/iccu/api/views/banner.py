from rest_framework import generics, permissions

from ...models import Banner
from ..serializers import PlaceBannerSerializer

__all__ = ("PlaceBannerView",)


class PlaceBannerView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PlaceBannerSerializer

    def get_object(self):
        return Banner.objects.get(is_active=True)
