# Generated by Django 3.0 on 2021-10-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20211030_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='HowToDo',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
