# Generated by Django 3.0 on 2021-10-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('free', 'Free'), ('pay only', 'Price')], default='free', max_length=100)),
            ],
        ),
    ]
