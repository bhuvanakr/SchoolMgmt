from django.urls import path, re_path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import SignUpView
from django.conf.urls import url

app_name = 'Schools'

urlpatterns = [
    path('', views.home, name='home'),
    path('password-change/',
         PasswordChangeView.as_view(template_name='registration/password-change.html'),
         name='password-change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='registration/password-change-success.html'),
         name='password-change-success'),
    re_path(r'^password_reset/$',
            PasswordResetView.as_view(template_name='registration/password_reset.html'),
            name='password_reset'),
    re_path(r'^password_reset/done/$',
            PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
            name='password_reset_done'),
    re_path(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmation.html'),
            name='password_reset_confirmation'),
    re_path(r'^password/reset/complete/$',
            PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
            name='password_reset_complete'),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('teacher/create/', views.teacher_create, name='teacher_create'),
    path('teacher/<int:pk>/edit/', views.teacher_edit, name='teacher_edit'),
    path('teacher/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    path('student_list/', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>delete/', views.student_delete, name='student_delete'),
    path('attendance_list/', views.attendance_list, name='attendance_list'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/<int:pk>/edit/', views.attendance_edit, name='attendance_edit'),
    path('attendance/<int:pk>delete/', views.attendance_delete, name='attendance_delete'),
    # path('attendance/count', views.attendance_count, name='attendance_count'),
]
