# Generated by Django 4.1.2 on 2024-10-24 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnapp', '0002_rename_firstname_person_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Repassword',
        ),
    ]
