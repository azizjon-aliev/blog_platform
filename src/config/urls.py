from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from src.config import settings
from . import swagger


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += swagger.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
