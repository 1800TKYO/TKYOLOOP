# Generated by Django 3.1.4 on 2021-01-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokyoloop', '0002_sample_cover_art'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tokyoloop/images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
