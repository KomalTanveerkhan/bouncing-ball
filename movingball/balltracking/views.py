# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyBall
from .serializers import MyBallSerializer
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
class MyBallList(APIView):
    def get(self, request):
        balls = MyBall.objects.all()
        serializer = MyBallSerializer(balls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# def index(request):
#     return render(request, 'index.html')

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to home page after successful login
#         else:
#             # Handle invalid login
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#     else:
#         return render(request, 'login.html')
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return self.get_redirect_url() or '/balltracking/abc/'



def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})