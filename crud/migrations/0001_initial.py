# Generated by Django 3.2.4 on 2021-06-29 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=64)),
                ('gender', models.CharField(blank=True, choices=[('DONT_KNOW', '모름'), ('FEMALE', '암컷'), ('MALE', '수컷')], max_length=20, null=True)),
                ('color', models.CharField(blank=True, choices=[('WHITE', '하얀색'), ('BLACK', '검은색'), ('GRAY', '회색'), ('YELLOW', '노란색')], max_length=20, null=True)),
                ('neutering', models.CharField(blank=True, choices=[('X', 'X'), ('DONT_KNOW', '모름'), ('O', 'O')], max_length=10, null=True)),
                ('friendly', models.CharField(default='0', max_length=64)),
                ('location', models.TextField()),
                ('cat_like', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(null=True)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image', to='crud.cat')),
            ],
        ),
    ]
