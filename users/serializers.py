from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'phone', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        del validated_data['password_confirm']
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        send_verification_email(user)
        return user

def send_verification_email(user):
    user.confirmation_code_generate()
    send_mail(
        'Email Verification Code',
        f'Your verification code is: {user.confirmation_code}',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        raise serializers.ValidationError("Incorrect email or password")
