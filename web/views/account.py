#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
from django.shortcuts import HttpResponse, render, redirect
from rbac.init_permission import init_permission
from rbac import models


def login(request):
    """
    登录视图
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "login.html")
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")

    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not current_user:
        return render(request, "login.html", {"msg": "用户名或密码错误"})

    request.session["user_id"] = current_user.pk

    init_permission(current_user, request)

    return redirect("/customer/list/")


# def index(request):
#     """
#     首页视图
#     :param request:
#     :return:
#     """
#     user_id = request.session.get("user_id")
#     menu_list = models.Role.objects.filter(userinfo__pk=user_id, permissions__menu=True).values_list("permissions__title")
#     print(user_id, menu_list)
#
#     return render(request, "layout.html", {"menu_list": menu_list})
