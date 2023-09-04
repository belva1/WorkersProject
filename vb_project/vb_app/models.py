from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50, default='', null=False)

    def __str__(self):
        return self.title


class Worker(models.Model):
    fullname = models.CharField(max_length=100, default='', null=False)
    work_code = models.CharField(max_length=3, default='', null=False, unique=True)
    mobile = models.IntegerField(blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.fullname