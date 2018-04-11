from rest_framework import serializers
from courses.models import TeacherProfile, CourseBase, CourseImage
from users.serializers import UserSerializer


class CourseBaseSerializer(serializers.ModelSerializer):
    """用户校验序列化类"""

    def validate(self, attrs):
        pass

    class Meta:
        model = CourseBase
        fields = '__all__'


class TeacherSerializer(CourseBaseSerializer):
    """用户序列化类"""
    user = UserSerializer()
    course = CourseBaseSerializer()

    class Meta:
        model = TeacherProfile
        fields = '__all__'


class CourseImageSerializer(serializers.ModelSerializer):
    """用户校验序列化类"""

    def validate(self, attrs):
        pass

    class Meta:
        model = CourseImage
        fields = '__all__'