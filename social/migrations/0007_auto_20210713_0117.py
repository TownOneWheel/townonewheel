# Generated by Django 3.2.4 on 2021-07-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20210713_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_at',
            field=models.TextField(null=True),
        ),
    ]
