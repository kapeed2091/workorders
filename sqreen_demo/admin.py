from django.contrib import admin

from .models import SqreenLog


@admin.register(SqreenLog)
class SqreenLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'data']
