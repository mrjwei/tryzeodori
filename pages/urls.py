from django.urls import path

from . import views


urlpatterns = [
    path('recruit/<uuid:pk>/delete/', views.RecruitDeleteView.as_view(), name='recruit_delete'),
    path('recruit/<uuid:pk>/edit/', views.RecruitUpdateView.as_view(), name='recruit_edit'),
    path('recruit/new/', views.RecruitCreateView.as_view(), name='recruit_new'),
    path('staff/<uuid:pk>/delete/', views.StaffDeleteView.as_view(), name='staff_delete'),
    path('staff/<uuid:pk>/edit/', views.StaffUpdateView.as_view(), name='staff_edit'),
    path('staff/new/', views.StaffCreateView.as_view(), name='staff_new'),
    path('saturday/<uuid:pk>/delete/', views.SaturdayDeleteView.as_view(), name='saturday_delete'),
    path('saturday/<uuid:pk>/edit/', views.SaturdayUpdateView.as_view(), name='saturday_edit'),
    path('saturday/new/', views.SaturdayCreateView.as_view(), name='saturday_new'),
    path('report/<uuid:pk>/delete/', views.ReportDeleteView.as_view(), name='report_delete'),
    path('report/<uuid:pk>/edit/', views.ReportUpdateView.as_view(), name='report_edit'),
    path('reports/', views.ReportListView.as_view(), name='reports'),
    path('report/new/', views.ReportCreateView.as_view(), name='report_new'),
    path('recruit/<uuid:pk>/delete/', views.RecruitDeleteView.as_view(), name='recruit_delete'),
    path('recruit/<uuid:pk>/edit/', views.RecruitUpdateView.as_view(), name='recruit_edit'),
    path('recruit/', views.RecruitListView.as_view(), name='recruit'),
    path('info/<uuid:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('info/<uuid:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('info/<uuid:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('info/new/', views.PostCreateView.as_view(), name='post_new'),
    path('info/', views.PostListView.as_view(), name='info'),
    path('', views.HomePageView.as_view(), name='home'),
]