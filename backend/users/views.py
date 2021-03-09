from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class LoginAPI(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        data = request.data

        email = str(data.get('email', None)).lower()
        password = data.get('password', None)

        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return Response({"ini": user.ini}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)


def login_as(request, user):
    if request.user.is_superuser:
        user = User.objects.get(pk=user)
        login(request, user)
    return redirect('/admin/')
