# Generated by Django 3.1.1 on 2020-09-29 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'permissions': [('can_view_all_reports', 'can view all reports')]},
        ),
    ]