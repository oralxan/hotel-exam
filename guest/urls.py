from django.urls import path,include
from .views import register_user, user_login, user_logout,LoginPage,my_post,SignupView
urlpatterns = [

    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/',my_post,name='my_post'),
    path('login/',LoginPage,name='LoginPage'),
    path('signup/', SignupView.as_view(), name='signup')

]