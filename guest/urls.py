# from django.urls import path,include
# from .views import register_user, user_login, user_logout,LoginPage,my_post,SignUpView
# urlpatterns = [

#     path('register/', register_user, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
#     path('account/', include('django.contrib.auth.urls')),
#     path('profile/',my_post,name='my_post'),
#     path('login/',LoginPage,name='logina'),
#     path('signup/', SignUpView.as_view(), name='signup'),

# ]
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import GuestRetrieveView
from .views import LoginPage,my_post,SignUpView

urlpatterns = [
    path('guest/<int:pk>/', GuestRetrieveView.as_view(), name='guest-retrieve'),
    # path('register/', register_user, name='register'),
    path('profile/',my_post,name='my_post'),
    path('login/',LoginPage,name='LoginPage'),
    path('signup/', SignUpView.as_view(), name='signup')

]
