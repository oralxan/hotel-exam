
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    path('guest/', include('guest.urls')),
    path('hotel/',include('hotel.urls')),
    path('room/',include('room.urls')),
 
]
urlpatterns = [
    path('admin/', admin.site.urls),

    path('booking/', include('booking.urls')),
    path('guest/',include("django.contrib.auth.urls")),
    path('guest/', include('guest.urls')),
    path('',include('hotel.urls')),
    path('room/',include('room.urls')),
    path('api/dj-rest-auth/',include('dj_rest_auth.urls'))
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)