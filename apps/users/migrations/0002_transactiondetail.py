# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-14 17:36
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20180414_1712'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='交易金额(0代表是分享用户)')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='交易产生时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseDetail', verbose_name='交易课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='交易用户')),
            ],
            options={
                'verbose_name': '交易明细',
                'verbose_name_plural': '交易明细',
            },
        ),
    ]
