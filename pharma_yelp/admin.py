from django.contrib import admin

from .models import UserRating


@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'comments', 'given_by', 'approval']

