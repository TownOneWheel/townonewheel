# Generated by Django 3.2.4 on 2021-07-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0022_auto_20210715_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='created_at',
            field=models.TextField(default=1626339042.8962505),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1626339042.8962505),
        ),
    ]
