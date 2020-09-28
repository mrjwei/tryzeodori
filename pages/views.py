from datetime import date
from datetime import timedelta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post, SaturdaySchedule, StaffSchedule, RecruitInfo, Report
from .forms import ReportForm, StaffForm, SaturdayForm, PostForm, RecruitForm

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


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    fields = ['title', 'content', 'tag']
    permission_required = 'pages.can_update_post'


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_update_post'


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


class RecruitUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RecruitInfo
    template_name = 'recruit_edit.html'
    success_url = reverse_lazy('recruit')
    login_url = 'account_login'
    fields = ['title', 'number', 'tag']
    permission_required = 'pages.can_update_recruit_info'


class RecruitDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = RecruitInfo
    template_name = 'recruit_delete.html'
    success_url = reverse_lazy('recruit')
    login_url = 'account_login'
    permission_required = 'pages.can_update_recruit_info'


class ReportListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    paginate_by = 2
    model = Report
    template_name = 'report_list.html'
    ordering = ['-date']
    login_url = 'account_login'
    permission_required = 'pages.can_view_all_reports'


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
        yesterday = date.today() - timedelta(days=1)
        if Report.objects.filter(author=self.request.user, created__gt=yesterday).exists():
            context['sent'] = True
        else:
            context['sent'] = False
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.author = self.request.user
        if (next := self.request.POST.get('next', '')) == 'confirm':
            return render(self.request, 'report_confirm.html', context)
        elif next == 'back':
            return render(self.request, 'report_new.html', context)
        elif next == 'send':
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('home'))


class ReportUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Report
    template_name = 'report_edit.html'
    success_url = reverse_lazy('reports')
    login_url = 'account_login'
    fields = ['name', 'condition', 'temperature', 'am', 'am_detail', 'pm', 'pm_detail', 'comment']
    permission_required = 'pages.can_view_all_reports'


class ReportDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Report
    template_name = 'report_edit.html'
    success_url = reverse_lazy('reports')
    login_url = 'account_login'
    permission_required = 'pages.can_view_all_reports'


class SaturdayCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SaturdayForm
    template_name = 'saturday_new.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_add_saturday_schedule'


class SaturdayUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = SaturdaySchedule
    template_name = 'saturday_edit.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    fields = '__all__'
    permission_required = 'pages.can_update_saturday_schedule'


class SaturdayDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = SaturdaySchedule
    template_name = 'saturday_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_update_saturday_schedule'
    

class StaffCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StaffForm
    template_name = 'staff_new.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_add_staff_schedule'


class StaffUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StaffSchedule
    template_name = 'staff_edit.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    fields = '__all__'
    permission_required = 'pages.can_update_staff_schedule'

class StaffDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = StaffSchedule
    template_name = 'staff_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    permission_required = 'pages.can_update_staff_schedule'