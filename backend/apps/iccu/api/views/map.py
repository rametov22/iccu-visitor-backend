from rest_framework import permissions, views
from rest_framework.response import Response

from ...models import Complex, Place
from ..serializers import ComplexSerializer, PlaceSerializer

__all__ = ("PlaceListView", "ComplexListView")


class PlaceListView(views.APIView):
    """Все места единым списком."""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        places = Place.objects.filter(is_active=True)
        return Response(PlaceSerializer(places, many=True, context={"request": request}).data)


class ComplexListView(views.APIView):
    """Места, сгруппированные по комплексам."""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        complexes = Complex.objects.filter(is_active=True).prefetch_related("places")
        return Response(ComplexSerializer(complexes, many=True, context={"request": request}).data)
