# Generated by Django 5.1.4 on 2024-12-15 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0002_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]