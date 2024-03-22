from rest_framework.viewsets import ViewSet
from .serializers import GuestSerializer
from rest_framework.response import Response
from rest_framework.status import *
from .models import Guest
from rest_framework import generics

class GuestRetrieveView(generics.RetrieveAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer



# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import GuestSerializer
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# from rest_framework.decorators import api_view
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status

# from .models import Guest

# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = GuestSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
    

#         user = None
#         if '@' in username:
#             try:
#                 user = Guest.objects.get(email=username)
#             except ObjectDoesNotExist:
#                 pass

#         if not user:
#             user = authenticate(username=username, password=password)

#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)

#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     if request.method == 'POST':
#         try:
#             request.user.auth_token.delete()
#             return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# ##############
# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User

# from hotel.models import Hotel
# from room.models import Model
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import CreateView
# from django.urls import reverse_lazy

# class SignupView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')
#     context_object_name = 'signup'
# def accounts(request, pk):
#     post =  Hotel.objects.filter(author=request.user)
#     host =  Hotel.objects.filter(author=request.user)
#     account = User.objects.get(username=request.user, id=pk)
#     context = {
#         'account': account,
#         'post': post,
#         'host' : host
#     }
#     return render(request, 'accounts/account.html', context)
from django.shortcuts import render
from booking.models import Booking
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm

def my_post(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(guest=request.user)  # "author" o'rniga "guest" nomli kalit so'zni ishlatish
        context = {
            'bookings': bookings
        }
        return render(request, 'accounts/account.html', context=context)
    else:
        return render(request, 'accounts/account.html')

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    context_object_name = 'signup'



def LoginPage(request):
    return render(request,'registration/login.html')



