#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from django.shortcuts import render, redirect, reverse, HttpResponse
from rbac import models
from rbac.forms.user import UserModeForm, UpdateUserModeForm, ResetPasswordUserModeForm


def user_list(request):
    """
    角色列表
    :param request:
    :return:
    """
    user_queryset = models.UserInfo.objects.all()

    return render(request, "rbac/user_list.html", {"users": user_queryset})


def user_add(request):
    """
    添加角色
    :param request:
    :return:
    """
    if request.method == "GET":
        form = UserModeForm()
        return render(request, "rbac/change.html", {'form': form})

    form = UserModeForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))

    return render(request, "rbac/change.html", {'form': form})


def user_edit(request, pk):
    """
    编辑角色
    :param request:
    :param pk: 要修改角色的ID
    :return:
    """
    obj = models.UserInfo.objects.filter(pk=pk).first()
    if not obj:
        return HttpResponse("用户不存在")
    if request.method == "GET":
        form = UpdateUserModeForm(instance=obj)
        return render(request, "rbac/change.html", {'form': form})

    form = UpdateUserModeForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))


def user_del(request, pk):
    """
    删除角色
    :param request:
    :param pk: 要删除角色的id
    :return:
    """
    origin_url = reverse('rbac:role_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel_url': origin_url})

    models.Role.objects.filter(id=pk).delete()

    return redirect(origin_url)


def user_reset_pwd(request, pk):
    """
    重置密码
    :param request:
    :param pk:
    :return:
    """
    obj = models.UserInfo.objects.filter(pk=pk).first()
    if not obj:
        return HttpResponse("用户不存在")
    if request.method == "GET":
        form = ResetPasswordUserModeForm()
        return render(request, "rbac/change.html", {'form': form})

    form = ResetPasswordUserModeForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))

    return render(request, "rbac/change.html", {'form': form})
