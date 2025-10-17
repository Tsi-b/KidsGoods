from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            access = response.data.get('access')
            refresh = response.data.get('refresh')
            response.set_cookie('access_token', access, httponly=True, secure=not settings.DEBUG, samesite='Lax')
            response.set_cookie('refresh_token', refresh, httponly=True, secure=not settings.DEBUG, samesite='Lax')
            response.data = {"detail":"Login successful"}
        return response


# class CookieTokenObtainPairView(TokenObtainPairView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         # response.data has access & refresh tokens
#         access = response.data.get('access')
#         refresh = response.data.get('refresh')
#         # Set cookies (httpOnly)
#         response.set_cookie(
#             key='access_token',
#             value=access,
#             httponly=True,
#             secure=not settings.DEBUG,    # secure cookie in production
#             samesite='Lax',
#             max_age=api_settings.ACCESS_TOKEN_LIFETIME.total_seconds()
#         )
#         response.set_cookie(
#             key='refresh_token',
#             value=refresh,
#             httponly=True,
#             secure=not settings.DEBUG,
#             samesite='Lax',
#             max_age=api_settings.REFRESH_TOKEN_LIFETIME.total_seconds()
#         )
#         # optionally remove tokens from response body
#         response.data = {"detail": "Login successful"}
#         return response

