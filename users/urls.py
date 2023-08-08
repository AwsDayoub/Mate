from django.urls import path , include
from . import views
app_name = 'users'

urlpatterns = [
    # Include Default auth urls
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('users/login/',views.LogInPage,name='LogInPage'),
    path('users/logout/',views.LogOutPage,name='LogOutPage')
]