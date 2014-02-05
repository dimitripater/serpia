from django.contrib import admin

from .models import CodeExamples


class CodeExamplesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(CodeExamples)