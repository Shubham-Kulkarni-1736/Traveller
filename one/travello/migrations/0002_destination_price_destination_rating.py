# Generated by Django 4.2.8 on 2023-12-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
