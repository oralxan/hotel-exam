from django.urls import path
from .views import (
    BookList,
    BookDetail,
    BookUpdate,
    BookDestroy,
    BookCreate,
    book_detaila,
    book_lista
)
urlpatterns =[
    path('booking/list/', BookList.as_view(),name='gift_list'),
    path('booking/detail/<int:pk>/', BookDetail.as_view(),name='gift_detail'),
    path('booking/create/', BookCreate.as_view(),name='gift_create'),
    path('booking/update/<int:pk>/', BookUpdate.as_view(),name='gift_update'),
    path('booking/delete/<int:pk>/', BookDestroy.as_view(),name='gift_destroy'),
    path('book/', book_lista,name='book_list'),
    path('book/<int:pk>/',book_detaila,name='book_detail'),


]