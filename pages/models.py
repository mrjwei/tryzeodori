import uuid
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField('テーマ', max_length=25)
    content = models.TextField('内容')
    publish_date = models.DateTimeField('公開日', auto_now=True, blank=False, null=True)
    TAGS = (
        ('New', '新着'),
    )
    tag = models.CharField('タッグ', max_length=10, blank=True, null=True, choices=TAGS)
    img = models.ImageField(upload_to='info/')

    class Meta:
        permissions = [
            ('can_add_post', 'can add post'),
            ('can_update_post', 'can update post'),
        ]
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
class SaturdaySchedule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField('内容', max_length=50)
    date = models.CharField('日付', max_length=20, blank=False)

    class Meta:
        permissions = [
            ('can_add_saturday_schedule', 'can add saturday schedule'),
            ('can_update_saturday_schedule', 'can update saturday schedule'),
        ]
    
    def __str__(self):
        return self.title
    
class StaffSchedule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField('名前', max_length=10)
    date = models.CharField('日付', max_length=20, blank=False)
    content = models.CharField('内容', max_length=10)
    duration = models.CharField('時間', max_length=20, blank=False)

    class Meta:
        permissions = [
            ('can_add_staff_schedule', 'can add staff schedule'),
            ('can_update_staff_schedule', 'can update staff schedule'),
        ]
    
    def __str__(self):
        return f'{self.name} {self.content}'


class RecruitInfo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField('タイトル', max_length=70)
    number = models.CharField('求人番号', max_length=25)
    publish_date = models.DateTimeField('公開日', auto_now=True, blank=False, null=True)
    TAGS = (
        ('New', '新着'),
    )
    tag = models.CharField('タッグ', max_length=10, blank=True, null=True, choices=TAGS)
    
    class Meta:
        permissions = [
            ('can_add_recruit_info', 'can add recruit info'),
            ('can_update_recruit_info', 'can update recruit info'),
        ]
    
    def __str__(self):
        return self.title


class Report(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    ) 
    date = models.DateField('日付', auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        verbose_name='ユーザー名',
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField('名前', max_length=10)
    CONDITION_CHOICES = (
        ('良い', '良い'),
        ('普通', '普通'),
        ('悪い', '悪い'),
    )
    condition = models.CharField('体調', max_length=10, choices=CONDITION_CHOICES, default='普通')
    temperature = models.DecimalField('体温', max_digits=3, decimal_places=1, default=36.0)
    TASKS = (
        ('テキスト学習', 'テキスト学習'),
        ('課題', '課題'),
        ('面談', '面談'),
        ('就職活動', '就職活動'),
        ('実習', '実習'),
        ('作業訓練', '作業訓練'),
        ('該当なし', '該当なし'),
        ('その他', 'その他'),
    )
    am = models.CharField('午前', max_length=20, choices=TASKS)
    am_detail = models.CharField('午前具体内容', max_length=100, blank=True)
    pm = models.CharField('午後', max_length=20, choices=TASKS)
    pm_detail = models.CharField('午後具体内容', max_length=100, blank=True)
    comment = models.CharField('感想や相談事など', max_length=150, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        permissions = [
            ('can_view_all_reports', 'can view all reports'),
        ]

    def __str__(self):
        return f'{self.date} {self.name}'