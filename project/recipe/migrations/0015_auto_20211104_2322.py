# Generated by Django 3.0 on 2021-11-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_auto_20211031_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='caloriePerUnit',
        ),
        migrations.AddField(
            model_name='recipe',
            name='price',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
