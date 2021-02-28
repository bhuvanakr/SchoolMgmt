from django.contrib import admin
from .models import Teacher, Student, Attendance


# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade',
                    'teacher_email', 'teacher_phone']
    list_filter = ['teacher_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade',
                   'teacher_email', 'teacher_phone']
    search_fields = ['teacher_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade',
                     'teacher_email', 'teacher_phone']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade',
                    'teacher']
    list_filter = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade',
                   'teacher']
    search_fields = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade',
                     'teacher']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['attendance_ID', 'student', 'status', 'date']
    list_filter = ['attendance_ID', 'student', 'status', 'date']
    search_fields = ['attendance_ID', 'student', 'status', 'date']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)