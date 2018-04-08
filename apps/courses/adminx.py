#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from xadmin import views
from courses.models import TeacherProfile, CourseBase, CourseImage, CourseDetail


class TeacherAdmin(object):
    list_display = ['user', 'description', 'course']


class CourseAdmin(object):
    list_display = ['title', 'course_desc', 'add_time', 'duration_time', 'class_num', 'play_num', 'up_num', 'cost_money']


class CourseDetailAdmin(object):
    list_display = ['course', 'subtitle', 'add_time', 'play_num', 'up_num', 'cost_money']


class CourseImageAdmin(object):
    list_display = ['index', 'course', 'image', 'add_time']


xadmin.site.register(TeacherProfile, TeacherAdmin)
xadmin.site.register(CourseBase, CourseAdmin)
xadmin.site.register(CourseDetail, CourseDetailAdmin)
xadmin.site.register(CourseImage, CourseImageAdmin)