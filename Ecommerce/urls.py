from django.contrib import admin
from django.urls import path,include #import include so that your file can be linked to other folders as well.
from django.conf import settings #add Settings to import files.
from django.conf.urls.static import static #for managing the static files.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
