# Generated by Django 4.0.3 on 2022-04-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
    ]