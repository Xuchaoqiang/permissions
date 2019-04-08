#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from django.conf.urls import url, include
from rbac.views import role, user, menu

app_name = 'rbac'
urlpatterns = [
    # 角色相关url
    url(r'^role/list/$', role.role_list, name='role_list'),
    url(r'^role/add/$', role.role_add, name='role_add'),
    url(r'^role/edit/(?P<pk>\d+)/$', role.role_edit, name='role_edit'),
    url(r'^role/del/(?P<pk>\d+)/$', role.role_del, name='role_del'),

    # 用户相关url
    url(r'^user/list/$', user.user_list, name='user_list'),
    url(r'^user/add/$', user.user_add, name='user_add'),
    url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
    url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
    url(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name='user_reset_pwd'),

    # 权限分配
    url(r'^menu/list/$', menu.menu_list, name='menu_list'),

]
