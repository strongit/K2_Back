from users.models import UserProfile
from users.serializers import UserSerializer, UserRegSerializer
from rest_framework import viewsets, mixins, permissions, status, authentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(nickname=username)|Q(username=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewSet(mixins.CreateModelMixin,  mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """用户视图，允许`create()`, `retrieve()`, `update()`"""
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    # authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # def get_serializer_class(self):
    #     if self.action == "retrieve":
    #         return UserRegSerializer
    #     elif self.action == "create":
    #         return UserSerializer
    #     return UserSerializer

    # def get_permissions(self):
    #     if self.action == "retrieve":
    #         return [permissions.IsAuthenticated()]
    #     elif self.action == "create":
    #         return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        re_dict = serializer.data
        print(re_dict)
        # payload = jwt_payload_handler(user)
        # re_dict["token"] = jwt_encode_handler(payload)
        # re_dict["name"] = user.nickname if user.nickname else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # def get_object(self):
    #     return self.request.user

    def perform_create(self, serializer):
        serializer.save()