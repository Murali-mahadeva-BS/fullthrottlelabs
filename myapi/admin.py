from django.contrib import admin
from .models import Userinfo, ActivityPeriod


class ActivityPeriodInline(admin.TabularInline):
    model = ActivityPeriod


class UserAdmin(admin.ModelAdmin):
    inlines = [
        ActivityPeriodInline,
    ]
    list_diaplay = '__all__'


admin.site.register(Userinfo, UserAdmin)
