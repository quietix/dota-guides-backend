from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, attrs):
        email = str(attrs.get('email')).lower()
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Please give both email and password.")

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exist.")

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError("Wrong Credentials.")

        attrs['user'] = user
        return attrs