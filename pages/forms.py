from functools import partial
from django.forms import ModelForm
from django.forms import Textarea
from django.forms import TextInput

from .models import Report
from .models import StaffSchedules
from .models import SaturdaySchedule
from .models import Post
from .models import RecruitInfo


class ReportForm(ModelForm):
    class Meta:
        model = Report
        exclude = ['id', 'date']
        widgets = {
            'comment': Textarea(),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id', 'publish_date']
        

CustomDateInput = partial(TextInput, {'class': 'datepicker'})

       
class SaturdayForm(ModelForm):
    class Meta:
        model = SaturdaySchedule
        fields = '__all__'
        widgets = {
            'date': CustomDateInput(),
        }
              

class StaffForm(ModelForm):
    class Meta:
        model = StaffSchedules
        fields = '__all__'
        widgets = {
            'date': CustomDateInput(),
        }
        
class RecruitForm(ModelForm):
    class Meta:
        model = RecruitInfo
        exclude = ['publish_date']