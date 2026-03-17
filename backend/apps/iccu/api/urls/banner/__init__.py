from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("banner/", views.PlaceBannerView.as_view(), name="place_banner"),
]
