# Generated by Django 3.2.4 on 2021-06-29 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20210629_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(blank=True, choices=[('GRAY', '회색'), ('WHITE', '하얀색'), ('BLACK', '검은색'), ('YELLOW', '노란색')], default='YELLOW', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', '수컷'), ('FEMALE', '암컷'), ('DONT_KNOW', '모름')], default='DONT_KHOW', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='neutering',
            field=models.CharField(blank=True, choices=[('O', 'O'), ('X', 'X'), ('DONT_KNOW', '모름')], default='DONT_KNOW', max_length=10, null=True),
        ),
    ]
