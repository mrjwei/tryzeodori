from django.contrib import admin

from .models import Post
from .models import SaturdaySchedule
from .models import StaffSchedule
from .models import RecruitInfo
from .models import Report

# Register your models here.
admin.site.register(Post)
admin.site.register(SaturdaySchedule)
admin.site.register(StaffSchedule)
admin.site.register(RecruitInfo)
admin.site.register(Report)