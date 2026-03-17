from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("schedule/", views.ScheduleView.as_view(), name="schedule"),
]
