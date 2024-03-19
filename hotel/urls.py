from django.urls import path
from .views import (
    HotelList,
    HotelDetail,
    HotelCreate,
    HotelUpdate,
    HotelDestroy,
    home_page,
    hotel_lista,
    hotel_detaila,
    hotel_createa,
    hotel_updatea,
    hotel_deletea
)
urlpatterns =[
    path('hotel/list/', HotelList.as_view(),name='gift_list'),
    path('hotel/detail/<int:pk>/', HotelDetail.as_view(),name='gift_detail'),
    path('hotel/create/', HotelCreate.as_view(),name='gift_create'),
    path('hotel/update/<int:pk>/', HotelUpdate.as_view(),name='gift_update'),
    path('hotel/delete/<int:pk>/', HotelDestroy.as_view(),name='gift_destroy'),
    path('',home_page, name='home_pagea'),
    path('hotel/', hotel_lista,name='hotel_list'),
    path('hotel/<int:pk>/',hotel_detaila,name='hotel_detail'),
    path('hotel/new/',hotel_createa,name='hotel_create'),
    path('hotel/update/<int:pk>/',hotel_updatea,name='hotel_update'),
    path('hotel/delete/<int:pk>/',hotel_deletea , name ='hotel_delete'),

]