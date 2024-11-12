from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class Department(models.Model):
#     id = models.CharField(verbose_name="mã khoa",
#                           max_length=255, unique=True, primary_key=True)
#     name = models.CharField(verbose_name="tên khoa",
#                             max_length=255, unique=True)

#     def __str__(self):
#         return self.id

#     class Meta:
#         verbose_name_plural = "khoa"


# class Classmate(models.Model):
#     class_id = models.CharField(
#         verbose_name="mã lớp", max_length=255, unique=True, primary_key=True)
#     name = models.CharField(verbose_name="tên lớp",
#                             max_length=255, unique=True)
#     url = models.SlugField(
#         max_length=255, verbose_name="quản lý lớp", null=True, blank=True)
#     # url = models.URLField(max_length=255, verbose_name="quản lý lớp", null=True, blank=True)

#     def __str__(self):
#         return "{}-{}".format(self.name, self.class_id)

#     class Meta:
#         verbose_name_plural = "lớp"

# class User(AbstractUser):
#   id = models.CharField(verbose_name="Mã sinh viên", primary_key=True ,unique=True, max_length=255)
#   avatar = models.ImageField(upload_to="avatar/%Y/%m/%d/", verbose_name="tên ảnh đại diện", blank=True, null=True)
#   email = models.EmailField(verbose_name="địa chỉ email", max_length=254, unique=True)
#   class_id = models.ForeignKey(Classmate, on_delete=models.CASCADE, verbose_name="lớp", null=True, blank=True)
#   role = models.IntegerField(verbose_name="phân quyền", default=3)
#   USERNAME_FIELD = "id"
#   REQUIRED_FIELDS = ["username", "email"]

#   def full_name(self):
#     return "{} {}".format(self.first_name, self.last_name)

#   def __str__(self):
#     return "{}-{} {}".format(self.id, self.first_name, self.last_name)
#   class Meta:
#     verbose_name_plural="người dùng"


# class User(AbstractUser):
#     id = models.CharField(verbose_name="Mã định danh",
#                           primary_key=True, unique=True, max_length=255)
#     isHashPassword = models.BooleanField(
#         verbose_name="Mật khẩu đã mã hóa", default=False)
#     avatar = models.ImageField(
#         verbose_name="Ảnh đại diện", upload_to="avatar/%Y/%m/%d/", blank=True, null=True)
#     email = models.EmailField(
#         verbose_name="Địa chỉ email", max_length=254, unique=True)
#     role = models.IntegerField(verbose_name="Phân quyền", default=3)
#     USERNAME_FIELD = "id"
#     REQUIRED_FIELDS = ["username", "email"]

        # def save(self, *args, **kwargs):
        #     user = super(User, self)
        #     if not user.isHashPassword:
        #       user.set_password(self.password)
        #       user.isHashPassword = True
        #       user.save(*args, **kwargs)
        #     return user

        # def full_name(self):
        #     return "{} {}".format(self.first_name, self.last_name)

        # def __str__(self):
        #     return "{}-{} {}".format(self.id, self.first_name, self.last_name)

        # class Meta:
        #     verbose_name_plural = "Người dùng"


# class Account(AbstractBaseUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     phone_number = models.CharField(max_length=50)

#     # required
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_superadmin = models.BooleanField(default=False)

#     USERNAME_FIELD = "email"    # Trường quyêt định khi login
#     REQUIRED_FIELDS = ["username", "first_name", "last_name"]    # Các trường yêu cầu khi đk tài khoản (mặc định đã có email), mặc định có password

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin    # Admin có tất cả quyền trong hệ thống

#     def has_module_perms(self, add_label):
#         return True

# class MyAccountManager(BaseUserManager):
#     def create_user(self, first_name, last_name, username, email, password=None):
#         if not email:
#             raise ValueError("Email address is required")

#         if not username:
#             raise ValueError("User name is required")

#         # Tạo đối tượng user mới
#         user = self.model(
#             email=self.normalize_email(email=email),    # Chuyển email về dạng bình thường
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, first_name, last_name, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email=email),
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.is_superadmin = True
#         user.save(using=self._db)
#         return user