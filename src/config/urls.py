from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from src.config import settings
from . import swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('src.apps.blog.urls')),
    path('api/v1/account/', include('src.apps.account.urls')),
]

urlpatterns += swagger.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
