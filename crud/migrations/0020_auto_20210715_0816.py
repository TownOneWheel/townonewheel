# Generated by Django 3.2.4 on 2021-07-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0019_auto_20210714_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='created_at',
            field=models.TextField(default=1626337010.539619),
        ),
        migrations.AlterField(
            model_name='cat',
            name='friendly',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1626337010.539619),
        ),
    ]