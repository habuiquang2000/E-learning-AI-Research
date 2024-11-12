from django.contrib import admin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
# from .models import (
#   User,
# )
# Register your models here.
# class AccountAdmin(UserAdmin):
#     list_display = ("email", "username", "first_name", "last_name", "last_login", "date_joined", "is_active")
#     list_display_links = ("email", "username", "first_name", "last_name")   # Các trường có gắn link dẫn đến trang detail
#     readonly_fields = ("last_login", "date_joined")     # Chỉ cho phép đọc
#     ordering = ("-date_joined",)     # Sắp xếp theo chiều ngược

#     # Bắt buộc phải khai báo
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
# admin.site.register(Account, AccountAdmin)


# class UserAdmin(ImportExportModelAdmin):   # FOR ADMIN IMPORT EXPORT ONLY 
#   class Meta:
#       model=User

# admin.site.register(User, UserAdmin)