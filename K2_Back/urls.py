"""K2_Back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
# from django.contrib import admin
import xadmin
from users.views import UserViewSet, getuserinfo
from courses.views import TeacherViewSet
import rest_framework
import pdb


router = DefaultRouter()

#配置users的url
# pdb.set_trace()
router.register(r'users', UserViewSet, base_name="users")
router.register(r'doctors', TeacherViewSet, base_name="doctors")


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^restframework/', include('rest_framework.urls', namespace='djangorestframework')),
    url(r'^users/getuserinfo/', getuserinfo),
    url(r'^', include(router.urls)),
]
