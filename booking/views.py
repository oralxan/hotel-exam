from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer
class BookList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer
class BookDetail(generics.RetrieveAPIView):
    queryset=Booking.objects.all()
    serializer_class = BookingSerializer
    
class BookCreate(generics.CreateAPIView):
    queryset=Booking.objects.all()
    serializer_class = BookingSerializer
class BookUpdate(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer
class BookDestroy(generics.DestroyAPIView):
    queryset=Booking.objects.all()
    serializer_class = BookingSerializer
    #####################################
from django.shortcuts import render,redirect
from .models import Booking
from .serializers import BookingSerializer
def book_lista(request):

    books = Booking.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/books_list.html', context=context)
def book_detaila(request,pk):
    book= Booking.objects.get(id=pk)
    context = {'book' : book}
    return render(request, 'book/book_detail.html',context=context )
