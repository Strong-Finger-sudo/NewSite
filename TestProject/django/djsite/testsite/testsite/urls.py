from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from testsite import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('beautysalon.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
