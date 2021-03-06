# Generated by Django 2.1.7 on 2019-04-07 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20190407_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='pid',
            field=models.ForeignKey(blank=True, help_text='对于非菜单权限需要选择一个可以称为菜单的权限， 用于做默认展开和选择菜单', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='rbac.Permission', verbose_name='关联的权限'),
        ),
    ]
