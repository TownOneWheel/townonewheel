# Generated by Django 3.2.4 on 2021-07-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0026_merge_20210723_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='created_at',
            field=models.TextField(default=1627286061.6998513),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1627286061.6998513),
        ),
    ]
