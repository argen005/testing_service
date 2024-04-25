from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserRegisterSerializer, UserLoginSerializer


User = get_user_model()


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        if not user.is_active:
            return Response({'error': 'Аккаунт не активирован'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'token': user.tokens()['access']}, status=status.HTTP_200_OK)


class VerifyEmail(APIView):
    def get(self, request, email, confirmation_code):
        user = User.objects.filter(email=email, confirmation_code=confirmation_code).first()
        if not user:
            return Response('Код верификации неверен', status=400)
        user.is_active = True
        user.confirmation_code = ''
        user.save()
        return Response('Верификация прошла успешно', status=200)
