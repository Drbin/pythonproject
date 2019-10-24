from django.db import models
from . import logs


class InitDb(models.Model):
    logs.logs_on("操作了数据库")
    name = models.CharField(max_length=20)
