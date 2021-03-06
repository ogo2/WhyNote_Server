from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from profile_user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chart.urls')),
    path('', include('profile_user.urls')),
    path('', include('artist.urls')),
    path('', include('magazine.urls')),
    path('', include('music.urls')),
    path('', include('search.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)