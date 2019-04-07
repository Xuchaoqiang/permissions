#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from django import forms
from django.core.exceptions import ValidationError
from rbac import models


class UserModeForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(UserModeForm, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        """
        检查密码是否一致
        :return:
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("两次输入密码不一致")
        return confirm_password


class UpdateUserModeForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'email', ]

    def __init__(self, *args, **kwargs):
        super(UpdateUserModeForm, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ResetPasswordUserModeForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['password', 'confirm_password', ]

    def __init__(self, *args, **kwargs):
        super(ResetPasswordUserModeForm, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        """
        检查密码是否一致
        :return:
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("两次输入密码不一致")
        return confirm_password
