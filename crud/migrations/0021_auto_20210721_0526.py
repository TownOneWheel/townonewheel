# Generated by Django 3.2.4 on 2021-07-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0020_auto_20210715_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='created_at',
            field=models.TextField(default=1626845170.164763),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1626845170.164763),
        ),
    ]
