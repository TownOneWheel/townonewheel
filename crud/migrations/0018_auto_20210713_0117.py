# Generated by Django 3.2.4 on 2021-07-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0017_auto_20210713_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='created_at',
            field=models.TextField(default=1626139021.0659194),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1626139021.0659194),
        ),
    ]
