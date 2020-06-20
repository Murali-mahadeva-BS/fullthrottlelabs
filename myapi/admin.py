from django.contrib import admin
from .models import Userinfo, ActivityPeriod


# admin.site.register(Userinfo)
# admin.site.register(ActivityPeriods)
class ActivityPeriodInline(admin.TabularInline):
    model = ActivityPeriod


class UserAdmin(admin.ModelAdmin):
    inlines = [
        ActivityPeriodInline,
    ]
    # list_display = ("real_name", "tz",)
    list_diaplay = '__all__'


admin.site.register(Userinfo, UserAdmin)
