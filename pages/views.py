from datetime import date
from datetime import timedelta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Post
from .models import SaturdaySchedule
from .models import StaffSchedule
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


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('publish_date')
        context['saturday_schedules'] = SaturdaySchedule.objects.all().order_by('date')
        context['staff_schedules'] = StaffSchedule.objects.all()
        return context

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'info.html'
    login_url = 'account_login'
    

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'
    login_url = 'account_login'
    

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'post_new.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_add_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = month
        context['day'] = day
        return context
    

class RecruitListView(LoginRequiredMixin, ListView):
    model = RecruitInfo
    context_object_name = 'posts'
    template_name = 'recruit.html'
    login_url = 'account_login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = month
        context['day'] = day
        return context
    

class RecruitCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RecruitForm
    template_name = 'recruit_new.html'
    success_url = reverse_lazy('recruit')
    login_url = 'account_login'
    permission_required = 'pages.can_add_recruit_info'


class ReportListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    paginate_by = 30
    model = Report
    context_object_name = 'reports'
    template_name = 'report_list.html'
    login_url = 'account_login'
    permission_required = 'pages.can_view_all_reports'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reports'] = Report.objects.all().order_by('date')
        return context


class ReportCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ReportForm
    template_name = 'report_new.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_add_report'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = month
        context['day'] = day
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.author = self.request.user
        yesterday = date.today() - timedelta(days=1)
        if Report.objects.filter(author=self.request.user, created__gt=yesterday).exists():
            return render(self.request, 'report_alert.html', context)
        else:
            if (next := self.request.POST.get('next', '')) == 'confirm':
                return render(self.request, 'report_confirm.html', context)
            elif next == 'back':
                return render(self.request, 'report_new.html', context)
            elif next == 'send':
                return super().form_valid(form)
            else:
                return redirect(reverse_lazy('home'))


class SaturdayCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SaturdayForm
    template_name = 'saturday_new.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_add_saturday_schedule'
    

class StaffCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StaffForm
    template_name = 'staff_new.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_add_staff_schedule'