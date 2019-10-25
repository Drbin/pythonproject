from django.db import models
from . import logs


class Admindb(models.Model):
    """用户"""

    no = models.IntegerField(primary_key=True, db_column='tbl_admin_id', verbose_name='用户id')
    name = models.CharField(max_length=20, db_column='tbl_admin_name', verbose_name='用户名称')
    location = models.CharField(max_length=10, db_column='tbl_admin_code', verbose_name='用户编号')

    class Meta:
        db_table = 'admin_tbl'



