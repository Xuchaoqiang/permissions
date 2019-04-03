#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
from django.shortcuts import HttpResponse, render, redirect
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

    permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id",
                                                                                      "permissions__url").distinct()
    print(permission_queryset)
    permission_list = [item["permissions__url"] for item in permission_queryset]
    print(permission_list)
    request.session["permission_url_list_key"] = permission_list

    return redirect("/customer/list/")
