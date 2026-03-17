from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("faq/", views.FAQView.as_view(), name="faq"),
]
