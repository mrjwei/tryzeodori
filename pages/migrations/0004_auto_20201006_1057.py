# Generated by Django 3.1.2 on 2020-10-06 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201005_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitinfo',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='recruitinfo',
            name='tag',
            field=models.CharField(blank=True, choices=[('New', '新着')], max_length=10, null=True, verbose_name='タグ'),
        ),
    ]
