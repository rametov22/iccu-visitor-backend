from rest_framework import generics, permissions

from ...models import TicketSource
from ..serializers import TicketSourceSerializer


class TicketSourceView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSourceSerializer

    def get_queryset(self):
        return TicketSource.objects.filter(is_active=True)
