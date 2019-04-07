#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from luffy_permission import settings


def init_permission(current_user, request):
    """
    初始化用户权限
    :return:
    """

    # 2. 权限信息初始化
    # 根据当前用户信息获取此用户所拥有的所有权限，并放入session。
    # 当前用户的所有权限
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id",
                                                                                      "permissions__title",
                                                                                      "permissions__url",
                                                                                      "permissions__name",
                                                                                      "permissions__pid",
                                                                                      "permissions__pid__title",
                                                                                      "permissions__pid__url",
                                                                                      "permissions__menu_id",
                                                                                      "permissions__menu__title",
                                                                                      "permissions__menu__icon").distinct()

    # 3. 获取权限+菜单信息
    permission_dict = {}

    menu_dict = {}

    for item in permission_queryset:

        permission_dict[item['permissions__name']] = {'id': item['permissions__id'],
                                                      'title': item['permissions__title'],
                                                      'url': item['permissions__url'],
                                                      'pid': item['permissions__pid'],
                                                      'p_title': item['permissions__pid__title'],
                                                      'p_url': item['permissions__pid__url']}

        menu_id = item["permissions__menu_id"]
        if not menu_id:
            continue
        node = {"id": item['permissions__id'], "title": item["permissions__title"], "url": item["permissions__url"]}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [node, ]
            }

    # permission_list = [item["permissions__url"] for item in permission_queryset]
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict
