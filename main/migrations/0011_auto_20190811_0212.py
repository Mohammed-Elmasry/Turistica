# Generated by Django 2.2.3 on 2019-08-11 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190811_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='open_from',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='open_to',
            field=models.TextField(),
        ),
    ]
