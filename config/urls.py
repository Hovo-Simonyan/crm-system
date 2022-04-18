from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/', include('crm.urls')),
]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    urlpatterns.extend(
        (
            path('admin/', admin.site.urls),
            path('api-auth/', include('rest_framework.urls')),
        )
    )