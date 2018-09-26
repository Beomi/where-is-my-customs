from django.contrib import admin

from .models import (
    KakaoUser,
    PackageQuery,
)


@admin.register(
    KakaoUser,
    PackageQuery,
)
class BaseAdmin(admin.ModelAdmin):
    pass
