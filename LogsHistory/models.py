from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.



class LogStatus(models.TextChoices):
    PROCESS = 'PROCESS', _('Đang xử lý')
    PENDDING = 'PENDDING', _('Chờ đợi')
    SUCCESS = 'SUCCESS', _('Thành công')
    ERROR = 'ERROR', _('Thất bại')



class Log(models.Model):  # Danh mục
    STATUS = models.CharField(
        verbose_name="Trạng thái",
        max_length=50,
        choices=LogStatus.choices,
        default=LogStatus.PROCESS,
    )
    METHOD = models.CharField(
        max_length=10,
        verbose_name="Phương thức"
    )
    SCHEME = models.CharField(
        max_length=8,
        verbose_name="SSL"
    )
    DOMAIN = models.CharField(
        max_length=255,
        verbose_name="Miền"
    )
    ENDPOINT = models.CharField(
        max_length=2000,
        verbose_name="Đường dẫn"
    )
    TIME = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Thời giann"
    )
    IP = models.CharField(
        max_length=255,
        verbose_name="Địa chỉ"
    )
    MACHINENAME = models.CharField(
        max_length=255,
        verbose_name="Tên máy"
    )
    MACHINEINFO = models.CharField(
        max_length=255,
        verbose_name="Thông tin thiết bị"
    )
