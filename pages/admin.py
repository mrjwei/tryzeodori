from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Post
from .models import SaturdaySchedule
from .models import StaffSchedule
from .models import RecruitInfo
from .models import Report


class ReportResource(resources.ModelResource):
    class Meta:
        model = Report
        exclude = ['id', 'author', 'created']


class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource

# Register your models here.
admin.site.register(Post)
admin.site.register(SaturdaySchedule)
admin.site.register(StaffSchedule)
admin.site.register(RecruitInfo)
admin.site.register(Report, ReportAdmin)