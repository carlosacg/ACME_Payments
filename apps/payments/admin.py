from django.contrib import admin
from apps.payments.models import Day, Schedule, Rate

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ['code', 'name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')
    search_fields = ['start_time', 'end_time']

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('day', 'schedule', 'price_by_hour')
    search_fields = ['day__code', 'price_by_hour']
    raw_id_fields = ["day", "schedule"]