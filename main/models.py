from django.db import models

class Trip(models.Model):
    trip_id = models.IntegerField(auto_created=True ,primary_key=True)
    trip_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_is_active = models.BooleanField(default=True)
    total_cost = models.DecimalField(max_digits=6)
    hours = models.IntegerField()
    extra_hours = models.FloatField()
    payment_way = [('Cash','Cash'),('Visa','Visa')]
    creation_date = models.DateTimeField(auto_now= True)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True,auto_created=True)
    category_name = models.CharField(blank=True)





