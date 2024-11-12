from django.db import models

# Create your models here.
"""
class DemoModel(models.Model):
    title = models.CharField(max_length=255,verbose_name = "tiêu đề")
    body = models.TextField(verbose_name = "viết mô tả")
    image = models.ImageField(upload_to="demo_images",verbose_name = "hình ảnh")

    def __str__(self):

        return self.title"""