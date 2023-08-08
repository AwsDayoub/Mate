from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('subject/<int:id>',views.subject,name='subject'),
    
]