from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from anverali_sites.settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-backend/', include('backend.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
