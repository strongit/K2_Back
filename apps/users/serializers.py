from rest_framework import serializers
from users.models import UserProfile


class UserSerializer(serializers.Serializer):
	"""用户序列化类"""
	class Meta:
		model = UserProfile
		fields = '__all__'