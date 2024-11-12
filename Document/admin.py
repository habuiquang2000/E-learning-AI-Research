# import csv
from django.contrib import admin
from _scope.base.admin import BaseInline, BaseAdmin
from .models import (
    Category,
    Subject,
    Chapter,
    Lesson
)
# Register your models here.


# CategoryAdmin

class SubjectInline(BaseInline):
    model = Subject

@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = (
        'title',
        'slug',
    )
    inlines = [SubjectInline]


# SubjectAdmin


class ChapterInline(BaseInline):
    model = Chapter

@admin.register(Subject)
class SubjectAdmin(BaseAdmin):
    list_display = (
        'title',
        'slug',
        'image'
    )

    inlines = [ChapterInline]

    # def get_queryset(self, request):
    #     return self.model.objects.filter(id=2)
#         return self.model.objects.filter(Chapter=request.Chapter)


# ChapterAdmin
class LessonInline(BaseInline):
    model = Lesson

@admin.register(Chapter)
class ChapterAdmin(BaseAdmin):
    list_display = (
        'title',
        'subject',
        'order',
        'slug',
    )

    inlines = [LessonInline]

#     def export_as_csv(self, request, queryset):
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
#             meta)
#         writer = csv.writer(response)

#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field)
#                                   for field in field_names])

#         return response


# LessonAdmin
@admin.register(Lesson)
class LessonAdmin(BaseAdmin):
    list_display = (
        'title',
        'chapter',
        'order',
        'slug',
    )


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Subject, SubjectAdmin)
# admin.site.register(Chapter, ChapterAdmin)
# admin.site.register(Lesson, LessonAdmin)


# class MySubjectAdmin(SubjectAdmin):
#     def __init__(self, *args, **kwargs):
#         super(CategoryView, self).__init__(*args, **kwargs)

#         # if not self.slug:
#         #     self.prepopulated_fields = {'slug': ('title',)}

#     def get_readonly_fields(self, request, obj=None):
#         fields = []
#         if obj:
#             fields += ['slug']

#         return fields
