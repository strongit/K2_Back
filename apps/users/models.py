from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    nickname = models.CharField(max_length=30, null=True, blank=True, verbose_name="用户昵称")
    avatarurl = models.CharField(max_length=30, null=True, blank=True, verbose_name="用户头像")
    gender = models.CharField(max_length=6, choices=(("1", u"男"), ("2", u"女"), ("0", u"未知")), default="1", verbose_name="用户性别")
    city = models.CharField(null=True, blank=True, max_length=30, verbose_name="用户所在城市")
    province = models.CharField(null=True, blank=True, max_length=30, verbose_name="用户所在省份")
    country = models.CharField(null=True, blank=True, max_length=30, verbose_name="用户所在国家")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.nickname  # TypeError: __str__ returned non-string (type NoneType)


class ShareDetail(models.Model):
    """
    记录有效分享明细
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="分享用户")
    shareTicket = models.CharField(verbose_name="shareTicket", max_length=255)
    groupName = models.CharField(verbose_name="转发群名", max_length=255)
    openGId = models.CharField(verbose_name="转发群id", max_length=255)  # 当 type="groupName" 时生效, 群id

    class Meta:
        verbose_name = "分享明细"
        verbose_name_plural = verbose_name

