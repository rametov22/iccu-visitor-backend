from django.urls import path

from ... import views

__all__ = ("urlpatterns",)


urlpatterns = [
    path("news/", views.news_list, name="news-list"),
    path("news/<int:news_id>/", views.news_detail, name="news-detail"),
    path("static/categories/", views.news_categories, name="static-categories"),
]
