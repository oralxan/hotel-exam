from .serializers import HotelSerializer
from .models import Hotel
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.shortcuts import render,redirect
class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


from django.shortcuts import render,redirect
from .models import Hotel
from .serializers import HotelSerializer




def home_page(request):
    return render(request,'hotel/home_pagea.html')

def hotel_lista(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/hotel_list.html', context=context)
def hotel_detaila(request,pk):
    hotel= Hotel.objects.get(id=pk)
    context = {'hotel' : hotel}
    return render(request, 'hotel/hotel_detail.html',context=context )
def hotel_createa(request):
    form = HotelSerializer()
    if request.method == 'POST':
        form = HotelSerializer(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
        return redirect('hotel_list')
    context = {
        'form':form
    }
    return render(request, 'hotel/hotel_create.html',context=context)
def hotel_updatea(request, pk):
    hotel =Hotel.objects.get(id=pk)
    form = HotelSerializer(instance=hotel)

    if request.method == 'POST':
        form = HotelSerializer(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save(commit=True)
            return redirect('hotel_list')

    context = {
        'form': form
    }
    return render(request, 'hotel/hotel_update.html', context=context)
def hotel_deletea(request,pk):
    hotel = Hotel.objects.get(id = pk)
    hotel.delete()
    return redirect('hotel_list')