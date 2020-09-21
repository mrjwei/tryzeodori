from datetime import date
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Post
from .models import SaturdaySchedule
from .models import StaffSchedules
from .models import RecruitInfo
from .models import Report
from .forms import ReportForm
from .forms import StaffForm
from .forms import SaturdayForm
from .forms import PostForm
from .forms import RecruitForm

today = date.today()
month = str(today.month)
day = str(today.day)

# Create your views here.
@login_required(login_url='account_login')
def home(request):
    posts = Post.objects.all().order_by('publish_date')
    saturday_schedules = SaturdaySchedule.objects.all().order_by('date')
    staff_schedules = StaffSchedules.objects.all()

    return render(
        request, 'home.html', 
        {
            'posts': posts, 
            'saturday_schedules': saturday_schedules,
            'staff_schedules': staff_schedules,
        })
    

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'info.html'
    login_url = 'account_login'
    

class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class RecruitPageView(LoginRequiredMixin, ListView):
    model = RecruitInfo
    context_object_name = 'posts'
    template_name = 'recruit.html'
    login_url = 'account_login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = month
        context['day'] = day
        return context


class ReportListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    paginate_by = 30
    model = Report
    context_object_name = 'reports'
    template_name = 'report_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reports'] = Report.objects.all().order_by('date')
        return context
    
    def test_func(self):
        self.request.user.has_perms['pages.can_view_all_reports']


@permission_required('pages.can_add_report')
@login_required(login_url='account_login')
def report_new(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('confirm', args=(obj.id,)))
    else:
        form = ReportForm()
    return render(
        request, 'report.html', 
        {'form': form, 'month': month, 'day': day})

class ConfirmPageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Report
    template_name = 'report_confirm.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.name == self.request

@permission_required('pages.can_add_post')  
@login_required(login_url='account_login')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/info/')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


@permission_required('pages.can_add_saturday_schedule') 
@login_required(login_url='account_login')
def saturday_new(request):
    if request.method == 'POST':
        form = SaturdayForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SaturdayForm()
    return render(request, 'saturday_new.html', {'form': form})


@permission_required('pages.can_add_staff_schedules') 
@login_required(login_url='account_login')
def staff_new(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StaffForm()
    return render(request, 'staff_new.html', {'form': form})


@permission_required('pages.can_add_recruit_info') 
@login_required(login_url='account_login')
def recruit_new(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/recruit/')
    else:
        form = RecruitForm()
    return render(request, 'recruit_new.html', {'form': form})