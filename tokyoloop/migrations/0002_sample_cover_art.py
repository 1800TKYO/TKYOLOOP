# Generated by Django 3.1.4 on 2021-01-07 00:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tokyoloop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='cover_art',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]