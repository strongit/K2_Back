from courses.models import TeacherProfile, CourseBase, CourseImage
from courses.serializers import TeacherSerializer, CourseBaseSerializer, CourseImageSerializer
from rest_framework import viewsets, mixins, permissions, status, authentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.


class TeacherViewSet(mixins.CreateModelMixin,  mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """讲师视图，允许`create()`, `retrieve()`, `update()`"""
    serializer_class = TeacherSerializer
    queryset = TeacherProfile.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TeacherSerializer
        elif self.action == "create":
            return TeacherSerializer

        return TeacherSerializer

    # def get_permissions(self):
    #     if self.action == "retrieve":
    #         return [permissions.IsAuthenticated()]
    #     elif self.action == "create":
    #         return []

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = self.perform_create(serializer.data)

        re_dict = serializer.data
        print(serializer.data)
        payload = jwt_payload_handler(teacher)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = teacher.user.nickname if teacher.user.nickname else teacher.user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # def get_object(self):
    #     return self.request.user

    def perform_create(self, validated_data):
        return TeacherProfile.objects.create(**validated_data)