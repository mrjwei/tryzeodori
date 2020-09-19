from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField('テーマ', max_length=25)
    content = models.TextField('内容')
    publish_date = models.DateTimeField('公開日', blank=False, null=True)
    TAGS = (
        ('new', '新着'),
    )
    tag = models.CharField('タッグ', max_length=10, blank=True, null=True, choices=TAGS)
    
    def __str__(self):
        return self.title
