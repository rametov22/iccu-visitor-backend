from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("rules/", views.RulesView.as_view(), name="rules"),
]
