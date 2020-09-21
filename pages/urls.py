from django.urls import path

from . import views


urlpatterns = [
    path('report/<uuid:pk>/confirm/', views.ConfirmPageView.as_view(), name='confirm'),
    path('recruit/new/', views.recruit_new, name='recruit_new'),
    path('staff/new/', views.staff_new, name='staff_new'),
    path('saturday/new/', views.saturday_new, name='saturday_new'),
    path('info/<uuid:pk>/', views.ConfirmPageView.as_view(), name='post_detail'),
    path('info/new/', views.post_new, name='post_new'),
    path('report/new/', views.report_new, name='report_new'),
    path('recruit/', views.RecruitPageView.as_view(), name='recruit'),
    path('info/', views.PostListView.as_view(), name='info'),
    path('', views.home, name='home'),
]