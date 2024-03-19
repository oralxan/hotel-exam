from django.urls import path
from .views import (
    RoomList,
    RoomCreate,
    RoomDetail,
    RoomDestroy,
    RoomUpdate,
    home_pagea,
    room_lista,
    room_createa,
    room_detaila,
    room_deletea,
    room_updatea
)
urlpatterns =[
    path('room/list/', RoomList.as_view(),name='room_list'),
    path('room/detail/<int:pk>/', RoomDetail.as_view(),name='room_detail'),
    path('room/create/', RoomCreate.as_view(),name='room_create'),
    path('room/update/<int:pk>/', RoomUpdate.as_view(),name='room_update'),
    path('room/delete/<int:pk>/', RoomDestroy.as_view(),name='room_destroy'),
    # path('rooms/', RoomList.as_view(), name='RoomList'),
    # path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('',home_pagea, name='home_page'),
    path('rooms/', room_lista,name='food_list'),
    path('rooms/<int:pk>/',room_detaila,name='food_detail'),
    path('rooms/new/',room_createa,name='food_create'),
    path('rooms/update/<int:pk>/',room_updatea,name='food_update'),
    path('rooms/delete/<int:pk>/', room_deletea , name ='food_delete'),
]

# from.views import (
#     home_pagea,
#     room_lista,
#     room_createa,
#     room_detaila,
#     room_deletea,
#     room_updatea
    
# )

# urlpatterns = [
#     path('',home_pagea, name='home_page'),
#     path('rooms/', room_lista,name='food_list'),
#     path('rooms/<int:pk>/',room_detaila,name='food_detail'),
#     path('rooms/new/',room_createa,name='food_create'),
#     path('rooms/update/<int:pk>/',room_updatea,name='food_update'),
#     path('rooms/delete/<int:pk>/', room_deletea , name ='food_delete'),
    

    
#]