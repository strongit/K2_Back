from users.models import UserProfile
from users.serializers import UserSerializer, UserRegSerializer
from rest_framework import viewsets, mixins, permissions, status, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# from utils.WXBizDataCrypt import WXBizDataCrypt
import urllib.request
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


@api_view(['GET', 'POST'])
def getuserinfo(request):
    """登录凭证校验"""
    appId = 'wx4f4bc4dec97d474b'
    secret = '47d4ed43a683f800e66169c09dd*****'
    sessionKey = 'tiihtNczf5v6AKRyjwEUhQ=='
    encryptedData = 'CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC+oNPdbB+3hVbJSRgv+4lGOETKUQz6OYStslQ142dNCuabNPGBzlooOmB231qMM85d2/fV6ChevvXvQP8Hkue1poOFtnEtpyxVLW1zAo6/1Xx1COxFvrc2d7UL/lmHInNlxuacJXwu0fjpXfz/YqYzBIBzD6WUfTIF9GRHpOn/Hz7saL8xz+W//FRAUid1OksQaQx4CMs8LOddcQhULW4ucetDf96JcR3g0gfRK4PC7E/r7Z6xNrXd2UIeorGj5Ef7b1pJAYB6Y5anaHqZ9J6nKEBvB4DnNLIVWSgARns/8wR2SiRS7MNACwTyrGvt9ts8p12PKFdlqYTopNHR1Vf7XjfhQlVsAJdNiKdYmYVoKlaRv85IfVunYzO0IKXsyl7JCUjCpoG20f0a04COwfneQAGGwd5oa+T8yO5hzuyDb/XcxxmK01EpqOyuxINew=='
    iv = 'r7BXXKkLb8qrSNn05n0qiA=='
    if request.method == 'POST':
        code = request.data
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&' \
              'grant_type=authorization_code' % (appId, secret, code['data'])
        r = urllib.request.urlopen(url)
        # pc = WXBizDataCrypt(appId, sessionKey)
        # print(pc.decrypt(encryptedData, iv))
        return Response(r.read(), status=status.HTTP_201_CREATED)
    else:
        return Response(None)


class UserViewSet(mixins.CreateModelMixin,  mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
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
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        re_dict = serializer.data
        # payload = jwt_payload_handler(user)
        # re_dict["token"] = jwt_encode_handler(payload)
        # re_dict["name"] = user.nickname if user.nickname else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # def get_object(self):
    #     return self.request.user

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
