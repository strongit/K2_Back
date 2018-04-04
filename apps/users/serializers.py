from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.Serializer):
    """用户序列化类"""

    class Meta:
        model = User
        fields = '__all__'


class UserRegSerializer(serializers.ModelSerializer):
    """用户校验序列化类"""

    def validate(self, attrs):
        pass

    class Meta:
        model = User
        fields = '__all__'
