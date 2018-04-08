from rest_framework import serializers
from courses.models import TeacherProfile, CourseBase, CourseImage


class TeacherSerializer(serializers.Serializer):
    """用户序列化类"""

    class Meta:
        model = TeacherProfile
        fields = '__all__'


class CourseBaseSerializer(serializers.Serializer):
    """用户校验序列化类"""

    def validate(self, attrs):
        pass

    class Meta:
        model = CourseBase
        fields = '__all__'


class CourseImageSerializer(serializers.Serializer):
    """用户校验序列化类"""

    def validate(self, attrs):
        pass

    class Meta:
        model = CourseImage
        fields = '__all__'