from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from mentorfind.email_auth import EmailBackend
from .serializers import CustomUserSerializerLogin, CustomUserSerializerRegister
from .models import CustomUser


class RegisterView(generics.CreateAPIView):
    """
        Registration function created with standart DRF registration    
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerRegister
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                password = request.data.get('password')
                user.set_password(password) #ДУЖЕ ВАЖЛИВА СТРОЧКА. Вона зашифровує пароль, а якщо його не шифрувати то нічого не робить
                user.save()

                token = Token.objects.create(user=user)
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    """
        Login function created with standart DRF registration    
    """

    serializer_class = CustomUserSerializerLogin

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # This line will trigger validation

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        email = serializer.validated_data.get('email')

        user = authenticate(request, username=username, password=password)
        if not user:
            user = EmailBackend().authenticate(request, email=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)