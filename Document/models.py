from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):  # Danh mục
    title = models.CharField(
        max_length=255,
        verbose_name="Tiêu đề danh mục"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Đường dẫn"
    )

    def save(self, *args, **kwargs):
        slug_param = slugify(self.title)
        gen_uuid = str(uuid4())[:8]

        self.slug = f"{slug_param}-{gen_uuid}"
        super(Category, self).save(*args, **kwargs)

    # @classmethod
    # def create(cls, _id, name, age, address, salary, join_date):
    #     test_record = cls(_id=_id, name=name, age=age,
    #                       adress=address, salary=salary, join_date=join_date)
        # return test_record

    # def publish(self):
    #     self.published_at = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title or ""

    class Meta:
        # managed = True
        # db_table = "book_example"
        # verbose_name = "Danh mục"
        verbose_name_plural = "Danh mục"


class Subject(models.Model):  # Môn học
    title = models.CharField(
        max_length=255,
        verbose_name="Tiêu đề môn"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Đường dẫn"
    )
    category = models.ForeignKey(
        to=Category,
        related_name="children",
        verbose_name="Danh mục",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    image = models.ImageField(
        upload_to="subject_images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Ảnh mô tả"
    )

    @property
    def as_dict(self):
        return {
            "id": self.id,
        }

    def save(self, *args, **kwargs):
        slug_param = slugify(self.title)
        gen_uuid = str(uuid4())[:8]

        self.slug = f"{slug_param}-{gen_uuid}"
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return self.title or ""

    class Meta:
        verbose_name_plural = "Môn học"


class Chapter(models.Model):  # Chương
    title = models.CharField(
        verbose_name="Tiêu đề chương",
        max_length=1000,
        blank=True,
        null=True
    )
    order = models.FloatField(
        verbose_name="Thứ tự",
        null=True,
        blank=True,
        default=None
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Đường dẫn"
    )
    subject = models.ForeignKey(
        to=Subject,
        related_name="children",
        verbose_name="Môn học",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    image = models.ImageField(
        verbose_name="Ảnh mô tả",
        upload_to="chapter_images/%Y/%m/%d/",
        null=True,
        blank=True
    )
    caption = RichTextField(
        verbose_name="Đầu đề",
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

    def save(self, *args, **kwargs):
        slug_param = slugify(self.title)
        gen_uuid = str(uuid4())[:8]

        self.slug = f"{slug_param}-{gen_uuid}"
        super(Chapter, self).save(*args, **kwargs)

    def __str__(self):
        return self.title or ""

    class Meta:
        verbose_name_plural = "Chương"
        ordering = (
            "subject",
            "order"
        )


class Lesson(models.Model):  # Bài Học
    title = models.CharField(
        verbose_name="Tiêu đề bài",
        max_length=1000,
        blank=True,
        null=True
    )
    order = models.FloatField(
        verbose_name="Thứ tự",
        null=True,
        blank=True,
        default=None
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Đường dẫn"
    )
    image = models.ImageField(
        verbose_name="Ảnh mô tả",
        upload_to="lesson_images/%Y/%m/%d/",
        null=True,
        blank=True
    )
    chapter = models.ForeignKey(
        to=Chapter,
        related_name="children",
        verbose_name="Chương",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    caption = models.TextField(
        verbose_name="Mô tả ngắn",
        blank=True,
        null=True
    )
    content = RichTextField(
        verbose_name="Nội dung",
        blank=True,
        null=True
    )
    audio_file = models.FileField(
        verbose_name="Âm thanh",
        upload_to="audio/%Y/%m/%d/",
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

    def save(self, *args, **kwargs):
        slug_param = slugify(self.title)
        gen_uuid = str(uuid4())[:8]

        self.slug = f"{slug_param}-{gen_uuid}"
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return self.title or ""

    class Meta:
        verbose_name_plural = "Bài học"
        ordering = (
            "chapter",
            "order"
        )

# class MySubject(Subject):
#     class Meta:
#         proxy = True
