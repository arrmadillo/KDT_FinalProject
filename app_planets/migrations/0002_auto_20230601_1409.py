# Generated by Django 3.2.18 on 2023-06-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_planets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planet',
            name='invite_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]