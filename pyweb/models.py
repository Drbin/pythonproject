from django.db import models


class InitDb(models.Model):
    name = models.CharField(max_length=20)
