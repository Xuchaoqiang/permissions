#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import re
from collections import OrderedDict
from django.template import Library
from django.shortcuts import reverse
from django.http import QueryDict
from luffy_permission import settings
from rbac.service import urls

register = Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    """
    创建一级菜单
    :return:
    """
    menu_list = request.session[settings.MENU_SESSION_KEY]
    return {'menu_list': menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    """
    创建二级菜单
    :param request:
    :return:
    """
    menu_dict = request.session[settings.MENU_SESSION_KEY]

    # 对字典的key进行排序
    key_list = sorted(menu_dict)

    # 空的有序字典
    ordered_dict = OrderedDict()

    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'

        for per in val['children']:
            if per['id'] == request.current_selected_permission:
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val

    return {'ordered_dict': ordered_dict}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
    """
    导航条菜单
    :param request:
    :return:
    """
    return {'record_list': request.breadcrumb}


@register.filter
def has_permission(request, name):
    """
    判断是否有权限
    :param request:
    :param name:
    :return:
    """
    if name in request.session[settings.PERMISSION_SESSION_KEY]:
        return True


@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    """
    生成带有原搜索条件的URL（替代了模板中的url）
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    return urls.memory_url(request, name, *args, **kwargs)