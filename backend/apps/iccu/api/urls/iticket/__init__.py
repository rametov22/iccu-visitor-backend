from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("iTicket/", views.iTicketView.as_view(), name="iTicket"),
]
