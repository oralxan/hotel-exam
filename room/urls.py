from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    RoomViewSet,
    home_pagea,
    room_lista,
    room_createa,
    room_detaila,
    room_deletea,
    room_updatea
)
router = DefaultRouter()
router.register('room', RoomViewSet, basename='room')

urlpatterns = []
urlpatterns =[
    # path('rooms/', RoomList.as_view(), name='RoomList'),
    # path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('',home_pagea, name='home_page'),
    path('rooms/', room_lista,name='food_list'),
    path('rooms/<int:pk>/',room_detaila,name='food_detail'),
    path('rooms/new/',room_createa,name='food_create'),
    path('rooms/update/<int:pk>/',room_updatea,name='food_update'),
    path('rooms/delete/<int:pk>/', room_deletea , name ='food_delete'),
]

urlpatterns += router.urls

