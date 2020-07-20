from django.contrib import admin
from .models import *


class HealthPrincipleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'img']
    list_display_links = list_display


class StatisticAdmin(admin.ModelAdmin):
    list_display = ['number', 'places', 'issues']
    list_display_links = list_display


admin.site.register(HealthPrinciple, HealthPrincipleAdmin)
admin.site.register(Statistic, StatisticAdmin)
