# Generated by Django 3.2.18 on 2023-05-26 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_planets', '0005_auto_20230524_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='need_confirm',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]
