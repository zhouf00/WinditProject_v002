from django.db import models
from django.contrib.auth import get_user_model

# from adm.models import Customer

User = get_user_model()

# Create your models here.

class WorkOrder(models.Model):
    type_choices = (('0', '初次安装'),('1', '售后服务'))
    status_choices = (('0', '工单已退回'),('1', '新建-保存'))
    number = models.CharField(max_length=10, verbose_name='工单号')
    title = models.CharField(max_length=50, verbose_name='标题')
    type = models.CharField(max_length=10, choices=type_choices)
    status = models.CharField(max_length=10, choices=status_choices)
    do_time = models.DateTimeField(default='', verbose_name='安排时间')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # content