# Generated by Django 5.1.5 on 2025-01-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('year_of_origin', models.IntegerField()),
            ],
        ),
    ]
