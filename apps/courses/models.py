from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from DjangoUeditor.models import UEditorField

User = get_user_model()

class CourseTag(models.Model):
    """
    课程类别
    """
    tag_name = models.CharField(max_length=30, verbose_name="类名")
    tag_desc = models.CharField(max_length=255, null=True, blank=True, verbose_name="类名描述")
    tag_index = models.IntegerField(default=0, unique=True, verbose_name="权重排序")  # 数字越小权重越大

    class Meta:
        verbose_name = "课程类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class TeacherProfile(models.Model):
    """
    讲师
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="讲师")
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name="讲师简介")

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class CourseBase(models.Model):
    """
    基础课程类
    """
    course_tag = models.ForeignKey(CourseTag, on_delete=models.CASCADE, verbose_name="课程分类")
    course_teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, verbose_name="课程医师")
    course_title = models.CharField(max_length=30, verbose_name="课程标题")
    course_desc = UEditorField(verbose_name=u"课程介绍", imagePath="course/images/", width=1000, height=300,
                               filePath="course/files/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="课程添加时间")
    duration_time = models.FloatField(null=True, blank=True, verbose_name="课程时长")
    class_num = models.IntegerField(null=True, blank=True, verbose_name="课时数")
    play_num = models.IntegerField(null=True, blank=True, verbose_name="播放量")
    up_num = models.IntegerField(null=True, blank=True, verbose_name="点赞量")
    cost_money = models.FloatField(null=True, blank=True, verbose_name="课程费用")

    class Meta:
        verbose_name = "课程基础信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course_title


class CourseDetail(models.Model):
    """
    详细课程类
    """
    course = models.ForeignKey(CourseBase, on_delete=models.CASCADE, verbose_name="课程标题")
    subtitle = models.CharField(max_length=300, null=True, blank=True, verbose_name="课时小标题")
    play_time = models.DateTimeField(default=datetime.now, verbose_name="课时上架时间")
    play_num = models.IntegerField(null=True, blank=True, verbose_name="播放量")
    up_num = models.IntegerField(null=True, blank=True, verbose_name="点赞量")
    cost_money = models.FloatField(null=True, blank=True, verbose_name="课程费用")

    class Meta:
        verbose_name = "课程详细信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.course_title + "：" + self.subtitle


class Comment(models.Model):
    """
    评论表
    """
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    course = models.ForeignKey(CourseDetail, verbose_name='评论课程', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='评论者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Reply(models.Model):
    """
    回复表
    """
    course = models.ForeignKey(CourseDetail, verbose_name="回复课程", on_delete=models.CASCADE)
    content = models.CharField(verbose_name="回复内容", max_length=255)
    user = models.ForeignKey(User, verbose_name="回复用户", on_delete=models.CASCADE)
    comment_reply = models.ForeignKey(Comment, verbose_name="回复评论", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "回复表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Up(models.Model):
    """
    记录赞表
    """
    course = models.ForeignKey(CourseDetail, verbose_name='点赞课程', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='点赞用户', on_delete=models.CASCADE)
    up = models.BooleanField(verbose_name='是否赞')

    class Meta:
        verbose_name = "记录赞表"
        verbose_name_plural = verbose_name


class Favorite(models.Model):
    """
    记录收藏表
    """
    course = models.ForeignKey(CourseDetail, verbose_name='收藏课程', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='收藏用户', on_delete=models.CASCADE)
    favorite = models.BooleanField(verbose_name='是否收藏')

    class Meta:
        verbose_name = "记录收藏表"
        verbose_name_plural = verbose_name


class Share(models.Model):
    """
    记录分享表
    """
    course = models.ForeignKey(CourseDetail, verbose_name='分享课程', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='分享用户', on_delete=models.CASCADE)
    share = models.IntegerField(null=True, blank=True, verbose_name='有效分享数')

    class Meta:
        verbose_name = "记录分享表"
        verbose_name_plural = verbose_name
        

class Question(models.Model):
    """
    患者提问
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    content = models.CharField(verbose_name="提问内容", max_length=255)
    image = models.ImageField(upload_to="question", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "患者提问"
        verbose_name_plural = verbose_name


class Answer(models.Model):
    """
    医师回复
    """
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, verbose_name="医师", related_name="teacher")
    content = models.CharField(verbose_name="答复内容", max_length=255)
    question_replay = models.ForeignKey(Question, verbose_name="答复疑问", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "医师回复"
        verbose_name_plural = verbose_name


class CourseImage(models.Model):
    """
    课程轮播图
    """
    course = models.ForeignKey(CourseBase, on_delete=models.CASCADE, verbose_name="课程", related_name="images")
    image = models.ImageField(upload_to="banner", verbose_name="图片", null=True, blank=True)
    index = models.IntegerField(default=0, verbose_name="轮播顺序")  # 0代表图片为候选轮播
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '课程图片'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.course.title
