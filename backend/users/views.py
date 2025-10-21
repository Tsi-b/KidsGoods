from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer

User = get_user_model()

# -------------------- REGISTER --------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# -------------------- LOGIN --------------------
class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            access = response.data.get('access')
            refresh = response.data.get('refresh')
            response.set_cookie(
                'access_token', access,
                httponly=True, secure=not settings.DEBUG, samesite='Lax'
            )
            response.set_cookie(
                'refresh_token', refresh,
                httponly=True, secure=not settings.DEBUG, samesite='Lax'
            )
            response.data = {"detail": "Login successful"}
        return response

# -------------------- PROTECTED ENDPOINT --------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({
        "message": f"Hello, {request.user.username}! You are authenticated."
    })
