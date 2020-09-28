# Generated by Django 3.1.1 on 2020-09-28 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=25, verbose_name='テーマ')),
                ('content', models.TextField(verbose_name='内容')),
                ('publish_date', models.DateTimeField(auto_now=True, null=True, verbose_name='公開日')),
                ('tag', models.CharField(blank=True, choices=[('New', '新着')], max_length=10, null=True, verbose_name='タッグ')),
            ],
            options={
                'permissions': [('can_add_post', 'can add post'), ('can_update_post', 'can update post')],
            },
        ),
        migrations.CreateModel(
            name='RecruitInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70, verbose_name='タイトル')),
                ('number', models.CharField(max_length=25, verbose_name='求人番号')),
                ('publish_date', models.DateTimeField(auto_now=True, null=True, verbose_name='公開日')),
                ('tag', models.CharField(blank=True, choices=[('New', '新着')], max_length=10, null=True, verbose_name='タッグ')),
            ],
            options={
                'permissions': [('can_add_recruit_info', 'can add recruit info'), ('can_update_recruit_info', 'can update recruit info')],
            },
        ),
        migrations.CreateModel(
            name='SaturdaySchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='内容')),
                ('date', models.CharField(max_length=20, verbose_name='日付')),
            ],
            options={
                'permissions': [('can_add_saturday_schedule', 'can add saturday schedule'), ('can_update_saturday_schedule', 'can update saturday schedule')],
            },
        ),
        migrations.CreateModel(
            name='StaffSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, verbose_name='名前')),
                ('date', models.CharField(max_length=20, verbose_name='日付')),
                ('content', models.CharField(max_length=10, verbose_name='内容')),
                ('duration', models.CharField(max_length=20, verbose_name='時間')),
            ],
            options={
                'permissions': [('can_add_staff_schedule', 'can add staff schedule'), ('can_update_staff_schedule', 'can update staff schedule')],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True, verbose_name='日付')),
                ('name', models.CharField(max_length=10, verbose_name='名前')),
                ('condition', models.CharField(choices=[('良い', '良い'), ('普通', '普通'), ('悪い', '悪い')], default='普通', max_length=10, verbose_name='体調')),
                ('temperature', models.DecimalField(decimal_places=1, default=36.0, max_digits=3, verbose_name='体温')),
                ('am', models.CharField(choices=[('テキスト学習', 'テキスト学習'), ('課題', '課題'), ('面談', '面談'), ('就職活動', '就職活動'), ('実習', '実習'), ('作業訓練', '作業訓練'), ('該当なし', '該当なし'), ('その他', 'その他')], max_length=20, verbose_name='午前')),
                ('am_detail', models.CharField(blank=True, max_length=100, verbose_name='午前具体内容')),
                ('pm', models.CharField(choices=[('テキスト学習', 'テキスト学習'), ('課題', '課題'), ('面談', '面談'), ('就職活動', '就職活動'), ('実習', '実習'), ('作業訓練', '作業訓練'), ('該当なし', '該当なし'), ('その他', 'その他')], max_length=20, verbose_name='午後')),
                ('pm_detail', models.CharField(blank=True, max_length=100, verbose_name='午後具体内容')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='感想や相談事など')),
                ('created', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー名')),
            ],
            options={
                'permissions': [('can_view_all_reports', 'can view all reports'), ('can_add_report', 'can add report')],
            },
        ),
    ]
