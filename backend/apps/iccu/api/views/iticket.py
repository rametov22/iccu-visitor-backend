from rest_framework import generics
from rest_framework.exceptions import NotFound

from ...models import iTicket
from ..serializers import iTicketSerializer

__all__ = ("iTicketView",)


class iTicketView(generics.RetrieveAPIView):
    serializer_class = iTicketSerializer

    def get_object(self):
        ticket = iTicket.objects.filter(is_active=True).first()
        if not ticket:
            raise NotFound("Not configured")
        return ticket
