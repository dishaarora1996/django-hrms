# Generated by Django 4.2.4 on 2023-08-24 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holiday',
            old_name='date',
            new_name='holiday_date',
        ),
    ]