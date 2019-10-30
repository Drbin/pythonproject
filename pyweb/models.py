from django.db import models
from . import logs


class AdminDb(models.Model):
    """用户"""
    logs.logs_on("模型被调用")
    id = models.IntegerField(primary_key=True, db_column='tbl_admin_id', verbose_name='用户id')
    name = models.CharField(max_length=40, db_column='tbl_admin_name', verbose_name='真实名称')
    u_name = models.CharField(max_length=40, db_column='tbl_admin_username', verbose_name='登录名')
    p_word = models.CharField(max_length=200, db_column='tbl_admin_password', verbose_name='用户编号')
    c_time = models.CharField(max_length=200, db_column='tbl_create_time', verbose_name='创建时间')
    l_time = models.CharField(max_length=200, db_column='tbl_login_time', verbose_name='登录时间')

    class Meta:
        # 告诉django不要数据库 删除 修改
        managed = False
        db_table = 'admin_tbl'


class NewsDb(models.Model):
    """用户"""
    logs.logs_on("模型被调用")
    id = models.IntegerField(primary_key=True, db_column='tbl_admin_id', verbose_name='用户id')
    name = models.CharField(max_length=40, db_column='tbl_admin_name', verbose_name='真实名称')
    u_name = models.CharField(max_length=40, db_column='tbl_admin_username', verbose_name='登录名')
    p_word = models.CharField(max_length=200, db_column='tbl_admin_password', verbose_name='用户编号')
    c_time = models.CharField(max_length=200, db_column='tbl_create_time', verbose_name='创建时间')
    l_time = models.CharField(max_length=200, db_column='tbl_login_time', verbose_name='登录时间')

    class Meta:
        # 告诉django不要数据库 删除 修改
        managed = False
        db_table = 'admin_tbl'

