from django.contrib import admin
from . import models

class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name']
    search_fields = ['city_name']
admin.site.register(models.City,CityAdmin)
