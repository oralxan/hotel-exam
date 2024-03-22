from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    BookingViewSet,
    book_detaila,
    book_lista
)
router = DefaultRouter()
router.register('booking', BookingViewSet, basename='booking')
urlpatterns = []
urlpatterns =[

    path('book/', book_lista,name='book_list'),
    path('book/<int:pk>/',book_detaila,name='book_detail'),


]
urlpatterns += router.urls