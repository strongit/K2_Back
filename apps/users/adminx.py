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
from .models import ShareDetail


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "固升小程序后台"
    site_footer = "固升骨健康"
    # menu_style = "accordion"


class ShareDetailAdmin(object):
    list_display = ['user', 'shareTicket', 'groupName']

xadmin.site.register(ShareDetail, ShareDetailAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)