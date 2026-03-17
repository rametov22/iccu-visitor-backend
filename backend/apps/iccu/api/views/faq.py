from rest_framework import permissions, views
from rest_framework.response import Response

from ...models import FAQ
from ..serializers import FAQSerializer

__all__ = ("FAQView",)


class FAQView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        faqs = FAQ.objects.filter(is_active=True)
        return Response(FAQSerializer(faqs, many=True).data)
