# Generated by Django 3.2.18 on 2023-05-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_planets', '0002_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='InappropriateWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30)),
            ],
        ),
    ]
