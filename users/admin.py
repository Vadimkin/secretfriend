# coding=utf-8
from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    # fields = ['name', 'vk_link', 'faculty', 'course', 'group_num', 'mobile_num']
    list_display = ['name', 'vk_link', 'faculty', 'course', 'group_num', 'mobile_num', 'is_active', 'friend']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Дозволити участь у грі"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=True)
    make_inactive.short_description = "Заборонити участь у грі"

    actions = [make_active, make_inactive, ]

admin.site.register(User, UserAdmin)