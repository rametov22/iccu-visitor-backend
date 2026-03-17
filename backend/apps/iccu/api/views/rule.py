from rest_framework import permissions, views
from rest_framework.response import Response

from ...models import RuleCategory
from ..serializers import RuleCategorySerializer

__all__ = ("RulesView",)


class RulesView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        categories = RuleCategory.objects.filter(is_active=True).prefetch_related("rules")
        return Response(RuleCategorySerializer(categories, many=True).data)
