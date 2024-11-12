from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Answer(models.Model):  # Trả lời
    keyword = models.CharField(  # Ngăn cách bằng dấu phẩy
        max_length=1000,
        verbose_name="Từ khóa",
        blank=True,
        null=True
    )
    content = models.CharField(
        max_length=1000,
        verbose_name="Câu trả lời",
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        verbose_name="Ngày tạo",
        auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name="Ngày sửa",
        auto_now=True
    )

    # @property
    # def get_text_price(self):
    #     return f"{self.price:,}"

    # def save(self, *args, **kwargs):
    #     slug_param = slugify(self.title)
    #     gen_uuid = str(uuid4())[:8]

    #     self.slug = f"{slug_param}-{gen_uuid}"
    #     super(Answer, self).save(*args, **kwargs)

    def __str__(self):
        return self.content or ""

    class Meta:
        verbose_name_plural = "Trả lời"


class Question(models.Model):  # Câu hỏi
    question = models.CharField(
        max_length=255,
        verbose_name="Câu hỏi"
    )
    answer = models.ForeignKey(
        to=Answer,
        related_name="children",
        verbose_name="Câu trả lời",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    user = models.ForeignKey(
        to=User,
        verbose_name="Người hỏi",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )

    created = models.DateTimeField(
        verbose_name="Ngày tạo",
        auto_now_add=True
    )

    # def save(self, *args, **kwargs):
    #     slug_param = slugify(self.title)
    #     gen_uuid = str(uuid4())[:8]

    #     self.slug = f"{slug_param}-{gen_uuid}"
    #     super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question or ""

    class Meta:
        verbose_name_plural = "Câu hỏi"
        ordering = (
            "id",
            "user",
            "created"
        )
