# Generated by Django 3.0 on 2021-10-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20211027_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='caloriePerUnit',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='type',
            field=models.CharField(choices=[('meat', 'Meat'), ('carbohydrate', 'Carbohydrate'), ('vegetable', 'Vegetable'), ('condiment', 'Condiment'), ('fruit', 'Fruit'), ('other', 'Other')], default='other', max_length=100),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
