# Generated by Django 3.0 on 2021-10-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]