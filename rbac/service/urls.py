#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from django.urls import reverse
from django.http import QueryDict


def memory_url(request, name, *args, **kwargs):
    """
    生成带有原搜索条件的URL（替代了模板中的url）
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    basic_url = reverse(name, args=args, kwargs=kwargs)     # 反解url的时候带参数（有名或者无名）

    # 当前URL中无参数
    if not request.GET:
        return basic_url

    query_dict = QueryDict(mutable=True)
    query_dict['_filter'] = request.GET.urlencode()

    return "%s?%s" % (basic_url, query_dict.urlencode())

def memory_reverse(request, name, *args, **kwargs):
    """
    反向生成URL
        http://127.0.0.1:8002/rbac/menu/add/?_filter=mid%3D6
        1. 在url中将原来的搜索条件，如filte后的值
        2. reverse生成原来的URL， 如：/menu/list
        3. /menu/add/?_filter=mid%3D6
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    url = reverse('rbac:menu_list')
    origin_params = request.GET.get('_filter')
    if origin_params:
        url = "%s?%s" % (url, origin_params)
    return url
