from django.urls import path

from . import views


urlpatterns = [
    path('recruit/new/', views.RecruitCreateView.as_view(), name='recruit_new'),
    path('staff/new/', views.StaffCreateView.as_view(), name='staff_new'),
    path('saturday/new/', views.SaturdayCreateView.as_view(), name='saturday_new'),
    path('reports/', views.ReportListView.as_view(), name='reports'),
    path('report/new/', views.ReportCreateView.as_view(), name='report_new'),
    path('recruit/', views.RecruitListView.as_view(), name='recruit'),
    path('info/<uuid:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('info/new/', views.PostCreateView.as_view(), name='post_new'),
    path('info/', views.PostListView.as_view(), name='info'),
    path('', views.HomePageView.as_view(), name='home'),
]