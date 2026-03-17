from decouple import config

__all__ = ("NEWS_API_URL",)


NEWS_API_URL = config("NEWS_API_URL")
