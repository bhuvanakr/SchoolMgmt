from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .views import SignUpView
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('password-change/',
         PasswordChangeView.as_view(template_name='registration/password-change.html'),
         name='password-change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='registration/password-change-success.html'),
         name='password-change-success'),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('teacher/create/', views.create_teacher, name='create_teacher'),
    path('edit/<int:pk>', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:teacher_id>', views.delete_teacher, name='delete_teacher'),
    path('student_list/', views.student_list, name='student_list'),
    path('student/create/', views.create_student, name='create_student'),
    path('edit/<int:pk>', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>', views.delete_student, name='delete_student'),
    # path('attendance/count', views.attendance_count, name='attendance_count'),
]
