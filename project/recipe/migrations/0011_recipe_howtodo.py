# Generated by Django 3.0 on 2021-10-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_remove_recipe_howtodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='HowToDo',
            field=models.TextField(blank=True),
        ),
    ]