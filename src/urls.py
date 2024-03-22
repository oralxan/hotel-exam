
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView

    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    path('guest/', include('guest.urls')),
    path('hotels/',include('hotel.urls')),
    path('room/',include('room.urls')),

    path('bookings/', include('booking.urls')),
    path('guests/',include("django.contrib.auth.urls")),
    path('guests/', include('guest.urls')),
    path('',include('hotel.urls')),
    path('rooms/',include('room.urls')),

    path('api/dj-rest-auth/',include('dj_rest_auth.urls')),
    #
    path('api/schema/', SpectacularAPIView.as_view(),name='schema' ),
    path('api/schema/redoc/',SpectacularRedocView.as_view(),name='redoc'),
    path('api/schema/swagger/',SpectacularSwaggerView.as_view(),name='swagger')
 ]
# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('booking/', include('booking.urls')),
#     path('guest/',include("django.contrib.auth.urls")),
#     path('guest/', include('guest.urls')),
#     path('',include('hotel.urls')),
#     path('room/',include('room.urls')),
#     path('api/dj-rest-auth/',include('dj_rest_auth.urls'))
# ]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)