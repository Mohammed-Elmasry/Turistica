# Generated by Django 2.2.3 on 2019-08-11 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tourist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('trans_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
    ]
