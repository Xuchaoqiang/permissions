#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from django import forms
from rbac import models


class RoleModeForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = ['title', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
