# Generated by Django 3.2.4 on 2021-07-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0013_merge_0010_auto_20210705_2353_0012_auto_20210705_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='location_lat',
            field=models.FloatField(default=37.54490018658278),
        ),
        migrations.AlterField(
            model_name='cat',
            name='location_lon',
            field=models.FloatField(default=127.05685028171477),
        ),
    ]
