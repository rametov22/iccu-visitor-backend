from rest_framework import serializers

from ...models import FAQ

__all__ = ("FAQSerializer",)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer"]
