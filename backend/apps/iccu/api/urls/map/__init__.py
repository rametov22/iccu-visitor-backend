from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("map/places/", views.PlaceListView.as_view(), name="place-list"),
    path("map/complexes/", views.ComplexListView.as_view(), name="complex-list"),
]
