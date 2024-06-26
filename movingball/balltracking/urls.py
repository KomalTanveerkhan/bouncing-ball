from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('ball_movement/', views.index, name='index'),
    path('ball_position_tracking/', views.MyBallList.as_view(),name='ball-position'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
]
