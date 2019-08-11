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

class TouristAdmin(admin.ModelAdmin):
    list_display = ['tourist_first_name','email','date_of_join']
    search_fields = ['tourist_first_name','tourist_last_name','email']
    list_filter = ['date_of_join']
    exclude = ['password','wallet']#it hide fields in admin form we will add all this fields in the future
admin.site.register(models.Tourist,TouristAdmin)

class TransportationAdmin(admin.ModelAdmin):
    list_display = ['trans_type']
    search_fields = ['trans_type']
admin.site.register(models.Transportation,TransportationAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language_name']
    search_fields = ['language_name']
admin.site.register(models.Language,LanguageAdmin)

class GuideAdmin(admin.ModelAdmin):
    list_display = ['guide_first_name','guide_last_name','guide_per_hour','date_of_join']
    exclude = ['password','wallet']
    list_filter = ['date_of_join']
    search_fields = ['guide_first_name','guide_last_name','language'
        ,'national_id','licence_id','date_of_join']
admin.site.register(models.Guide,GuideAdmin)

class TripAdmin(admin.ModelAdmin):
    list_display = ['trip_number','start_date','end_date',
                    'start_time','end_time','creation_date','status_is_active']
    list_filter = ['creation_date','category','city','transportation','guide','site']
    search_fields = ['trip_id','trip_number',
                     'creation_date','category','city','transportation','guide']
    list_editable = ['status_is_active']
admin.site.register(models.Trip,TripAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    search_fields = ['category_name']
admin.site.register(models.Category,CategoryAdmin)

