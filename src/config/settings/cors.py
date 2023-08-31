import os

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CORS_ALLOWED_ORIGINS").split(",")

CORS_ALLOWED_ORIGINS = os.getenv("DJANGO_CORS_ALLOWED_ORIGINS").split(",")

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)