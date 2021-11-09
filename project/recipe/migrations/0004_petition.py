# Generated by Django 3.2.9 on 2021-11-08 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0003_auto_20211108_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='petition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petition', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('confirm', models.CharField(choices=[('no', 'No'), ('confirm', 'Confirm')], default='no', max_length=10)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
