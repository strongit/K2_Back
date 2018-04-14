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
from courses.models import TeacherProfile, CourseBase, CourseImage, CourseDetail, Comment, Reply, Question, Answer, CourseTag


class TeacherAdmin(object):
    list_display = ['user', 'description']


class CourseBaseAdmin(object):
    list_display = ['course_tag', 'course_teacher', 'course_title', 'course_desc', 'add_time', 'duration_time', 'class_num', 'play_num', 'up_num', 'cost_money']


class CourseDetailAdmin(object):
    list_display = ['course', 'subtitle', 'play_time', 'play_num', 'up_num', 'cost_money']


class CourseImageAdmin(object):
    list_display = ['index', 'course', 'image', 'add_time']


class CommentAdmin(object):
    list_display = ['course', 'user', 'content', 'create_time']


class ReplyAdmin(object):
    list_display = ['course', 'user', 'content', 'comment_reply']


class CourseTagAdmin(object):
	list_display = ['tag_name', 'tag_desc', 'tag_index']


xadmin.site.register(CourseTag, CourseTagAdmin)
xadmin.site.register(TeacherProfile, TeacherAdmin)
xadmin.site.register(CourseBase, CourseBaseAdmin)
xadmin.site.register(CourseDetail, CourseDetailAdmin)
xadmin.site.register(CourseImage, CourseImageAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Reply, ReplyAdmin)