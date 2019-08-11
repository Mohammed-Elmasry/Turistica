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
    category_name = models.CharField(blank=True,max_length=32)

class Site(models.Model):
    site_id = models.IntegerField(primary_key=True ,auto_created=True)
    site_name = models.CharField(blank=True ,max_length=32)
    open_from = models.DateTimeField()
    open_to = models.DateTimeField()
    site_cost = models.DecimalField(max_digits=4 ,decimal_places=2)

class Tourist(models.Model):
    tourist_id = models.IntegerField(primary_key=True ,auto_created=True)
    tourist_first_name = models.CharField(max_length=32,blank=True)
    tourist_last_name = models.CharField(max_length=32 , blank=True)
    date_of_birth = models.DateField()
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
    date_of_join = models.DateField(auto_now=True)
    wallet = models.DecimalField(max_length=6,decimal_places=None)

class City(models.Model):
    city_id = models.IntegerField(primary_key=True,auto_created=True)
    city_name = models.CharField(blank=True)


class Transportation(models.Model):
    trans_id = models.IntegerField(primary_key=True,auto_created=True)
    trans_type = [('Public Transportation','public'),('Private Transportation','private')]

class Guide(models.Model):
    guide_id = models.IntegerField(primary_key=True , auto_created=True)
    guide_first_name = models.CharField(max_length=32,blank=True)
    guide_last_name = models.CharField(max_length=32 ,blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    bank_account = models.CharField()
    wallet = models.DecimalField(max_digits=6 ,decimal_places=None)
    guide_per_hour = models.DecimalField(max_digits=6)
    national_id = models.CharField(max_length=13)
    licence_id = models.CharField()#we need to know the max_length of licence_id

