from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("ticket-sources/", views.TicketSourceView.as_view(), name="ticket-source"),
]
