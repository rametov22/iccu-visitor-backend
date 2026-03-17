from rest_framework import permissions, views
from rest_framework.response import Response

from ...models import Schedule
from ..serializers import ScheduleDaySerializer

__all__ = ("ScheduleView",)


class ScheduleView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        days = Schedule.objects.all()
        today = Schedule.today()

        return Response(
            {
                "schedule": ScheduleDaySerializer(days, many=True).data,
                "today": ScheduleDaySerializer(today).data if today else None,
            }
        )
