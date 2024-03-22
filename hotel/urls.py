from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    HotelViewSet,
    home_page,
    hotel_lista,
    hotel_detaila,
    hotel_createa,
    hotel_updatea,
    hotel_deletea
)
router = DefaultRouter()
router.register('hotels/', HotelViewSet, basename='hotel')
urlpatterns = []
urlpatterns =[
    path('',home_page, name='home_pagea'),
    path('hotel/', hotel_lista,name='hotel_list'),
    path('hotel/<int:pk>/',hotel_detaila,name='hotel_detail'),
    path('hotel/new/',hotel_createa,name='hotel_create'),
    path('hotel/update/<int:pk>/',hotel_updatea,name='hotel_update'),
    path('hotel/delete/<int:pk>/',hotel_deletea , name ='hotel_delete'),

]
urlpatterns += router.urls