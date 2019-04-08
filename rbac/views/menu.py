#!-*- coding:utf-8 -*-
# __author__:"irving"

from django.shortcuts import render, redirect, reverse, HttpResponse
from rbac import models


def menu_list(request):
    """
    权限分配菜单展示
    :param request:
    :return:
    """
    menus = models.Menu.objects.all()
    menu_id = request.GET.get('mid')

    return render(
        request,
        "rbac/menu_list.html",
        {'menus': menus,
         'menu_id': menu_id}
    )
