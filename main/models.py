from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(blank=True, max_length=32)

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=32,blank=True)

class Site(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField(blank=True, max_length=32)
    open_from = models.TimeField()
    open_to = models.TimeField()
    site_cost = models.DecimalField(max_digits=6, decimal_places=2)


class Tourist(models.Model):
    tourist_id = models.AutoField(primary_key=True)
    tourist_first_name = models.CharField(max_length=32, blank=True, null=False)
    tourist_last_name = models.CharField(max_length=32, blank=True,null=False)
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
    date_of_join = models.DateField(auto_now=True)
    wallet = models.DecimalField(max_digits=6, decimal_places=2)


class Transportation(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_type = [('Public Transportation', 'public'), ('Private Transportation', 'private')]


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    language_name = [('English', 'English'), ('Arabic', 'Arabic'),
                     ('German', 'German'), ('Italian', 'Italian'),
                     ('Russian', 'Russian'), ('Turkish', 'Turkish'),
                     ('Swedish', 'Swedish'), ('Greek', 'Greek'),
                     ('French', 'French')]

class Guide(models.Model):
    language = models.ManyToManyField(Language,blank=True)
    guide_id = models.AutoField(primary_key=True)
    guide_first_name = models.CharField(max_length=32, blank=True,null=False)
    guide_last_name = models.CharField(max_length=32, blank=True,null=False)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=False)
    bank_account = models.CharField(null=False,max_length=30)
    wallet = models.DecimalField(max_digits=6, decimal_places=2)
    guide_per_hour = models.DecimalField(max_digits=6,null=False,decimal_places=2)
    national_id = models.CharField(max_length=13,null=False)
    licence_id = models.CharField(null=False,max_length=30)  # we need to know the max_length of licence_id


class GuidePhotoData(models.Model):
    guide = models.OneToOneField(Guide,on_delete=models.CASCADE,primary_key=True)
    criminal_certificate = models.ImageField()
    national_card = models.ImageField()
    guide_licence = models.ImageField()



class Trip(models.Model):
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)
    city = models.ForeignKey(City , on_delete=models.CASCADE)
    tourist = models.ForeignKey(Tourist , on_delete=models.CASCADE)
    transportation = models.ForeignKey(Transportation ,on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide,on_delete=models.CASCADE)
    site = models.ManyToManyField(Site,blank=True)
    trip_id = models.AutoField( primary_key=True)
    trip_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_is_active = models.BooleanField(default=True)
    total_cost = models.DecimalField(max_digits=6,decimal_places=2)
    hours = models.IntegerField()
    extra_hours = models.FloatField()
    payment_way = [('Cash', 'Cash'), ('Visa', 'Visa')]
    creation_date = models.DateTimeField(auto_now=True)
