# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-05 21:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='up',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='点赞用户'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseBase', verbose_name='课程列表'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='reply',
            name='comment_reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Comment', verbose_name='回复评论'),
        ),
        migrations.AddField(
            model_name='reply',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseDetail', verbose_name='回复课程'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='回复用户'),
        ),
        migrations.AddField(
            model_name='courseimage',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='courses.CourseBase', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseBase', verbose_name='课程标题'),
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseDetail', verbose_name='评论课程'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者'),
        ),
    ]