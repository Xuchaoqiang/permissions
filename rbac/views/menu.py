#!-*- coding:utf-8 -*-
# __author__:"irving"

from django.shortcuts import render, redirect, reverse, HttpResponse
from rbac import models
from rbac.forms.menu import MenuModeForm, SecondMenuModeForm
from rbac.service.urls import memory_reverse


def menu_list(request):
    """
    权限分配菜单展示
    :param request:
    :return:
    """
    menus = models.Menu.objects.all()
    menu_id = request.GET.get('mid')  # 用户选择的一级菜单
    second_menu_id = request.GET.get('sid')    # 用户选择的二级菜单

    if menu_id:
        second_menus = second_menus = models.Permission.objects.filter(menu=menu_id)
    else:
        second_menus = []

    return render(
        request,
        "rbac/menu_list.html",
        {
            'menus': menus,
            'menu_id': menu_id,
            'second_menus': second_menus,
            'second_menu_id': second_menu_id
        }
    )


def menu_add(request):
    """
    添加一级菜单
    :param request:
    :return:
    """
    if request.method == "GET":
        form = MenuModeForm()
        return render(request, "rbac/change.html", {'form': form})

    form = MenuModeForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, "rbac/change.html", {'form': form})


def menu_edit(request, pk):
    """
    编辑一级菜单
    :param request:
    :param pk: 要修改角色的ID
    :return:
    """
    obj = models.Menu.objects.filter(pk=pk).first()
    if not obj:
        return HttpResponse("角色不存在")
    if request.method == "GET":
        form = MenuModeForm(instance=obj)
        return render(request, "rbac/change.html", {'form': form})

    form = MenuModeForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))


def menu_del(request, pk):
    """
    删除一级菜单
    :param request:
    :param pk: 要删除角色的id
    :return:
    """
    url = memory_reverse(request, 'rbac:menu_list')

    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel_url': url})

    models.Menu.objects.filter(id=pk).delete()

    return redirect(url)


def second_menu_add(request, menu_id):
    """
    添加二级菜单
    :param request:
    :param menu_id: 已选择的一级菜单ID（用于设置默认值）
    :return:
    """
    menu_object = models.Menu.objects.filter(id=menu_id).first()

    if request.method == "GET":
        form = SecondMenuModeForm(initial={'menu': menu_object})
        return render(request, "rbac/change.html", {'form': form})

    form = SecondMenuModeForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, "rbac/change.html", {'form': form})


def second_menu_edit(request, pk):
    """
    编辑二级菜单
    :param request:
    :param pk: 当前要编辑的二级菜单
    :return:
    """
    permission_object = models.Permission.objects.filter(pk=pk).first()

    if request.method == "GET":
        form = SecondMenuModeForm(instance=permission_object)
        return render(request, "rbac/change.html", {'form': form})

    form = SecondMenuModeForm(instance=permission_object, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))


def second_menu_del(request, pk):
    """
    删除一级菜单
    :param request:
    :param pk: 当前要删除的二级菜单
    :return:
    """
    url = memory_reverse(request, 'rbac:menu_list')

    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel_url': url})

    models.Permission.objects.filter(id=pk).delete()

    return redirect(url)