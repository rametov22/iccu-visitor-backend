from django.urls import include, path

from . import banner, faq, iticket, map, news, rule, schedule, ticket

__all__ = ("urlpatterns",)


urlpatterns = [
    # path("", include(banner)),
    path("", include(schedule)),
    # path("", include(ticket)),
    path("", include(news)),
    path("", include(iticket)),
    path("", include(rule)),
    path("", include(faq)),
    path("", include(map)),
]
