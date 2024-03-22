from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.shortcuts import render,redirect
from .models import Room
from .serializers import RoomSerializer
# class RoomList(generics.ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class=RoomSerializer
# class RoomDetail(generics.RetrieveAPIView):
#     queryset=Room.objects.all()
#     serializer_class = RoomSerializer
# class RoomCreate(generics.CreateAPIView):
#     queryset=Room.objects.all()
#     serializer_class = RoomSerializer
# class RoomUpdate(generics.UpdateAPIView):
#     queryset = Room.objects.all()
#     serializer_class=RoomSerializer
# class RoomDestroy(generics.DestroyAPIView):
#     queryset=Room.objects.all()
#     serializer_class =RoomSerializer
class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


###############################################
def home_pagea(request):
    return render(request,'room/home_page.html')

def room_lista(request):

    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room/room_list.html', context=context)
def room_detaila(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'room/room_detail.html',context=context )
def room_createa(request):
    form = RoomSerializer()
    if request.method == 'POST':
        form = RoomSerializer(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
        return redirect('room_list')
    context = {
        'form':form
    }
    return render(request, 'room/room_create.html',context=context)
def room_updatea(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomSerializer(instance=room)

    if request.method == 'POST':
        form = RoomSerializer(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save(commit=True)
            return redirect('food_list')

    context = {
        'form': form
    }
    return render(request, 'room/room_update.html', context=context)
def room_deletea(request,pk):
    room = Room.objects.get(id = pk)
    room.delete()
    return redirect('room_list')