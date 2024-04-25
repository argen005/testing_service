from django.urls import path
from users.views import UserRegisterAPIView, UserLoginAPIView, VerifyEmail

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('activate/<str:email>/<str:confirmation_code>/', VerifyEmail.as_view(), name='activate'),
]
