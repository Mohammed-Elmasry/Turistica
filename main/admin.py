from django.contrib import admin
from . import models

class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name']
    search_fields = ['city_name']
admin.site.register(models.City,CityAdmin)

class SiteAdmin(admin.ModelAdmin):
    list_display = ['site_name','open_from','open_to','site_cost']
    search_fields = ['site_name']
    list_filter = ['site_name','open_from','open_to','site_cost']
    list_editable = ['open_from','open_to']
admin.site.register(models.Site , SiteAdmin)