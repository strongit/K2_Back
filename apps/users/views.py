from django.shortcuts import render
from users.models import UserProfile
from users.serializers import UserSerializer
from rest_framework import viewsets, mixins, status
# Create your views here.

class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""用户视图"""
	serializer_class = UserSerializer
	queryset = UserProfile.objects.all()
		