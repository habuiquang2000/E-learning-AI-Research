from django.contrib import admin


class BaseInline(admin.StackedInline):
    exclude = (
        "slug",
    )
    readonly_fields = (
        "slug",
    )


class BaseAdmin(admin.ModelAdmin):
    exclude = (
        "slug",
    )
    readonly_fields = (
        "slug",
    )
