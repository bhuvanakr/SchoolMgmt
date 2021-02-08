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
                    'student_teacher_ID']
    list_filter = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade',
                   'student_teacher_ID']
    search_fields = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade',
                     'student_teacher_ID']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['Attendance_student_ID', 'status', 'date']
    list_filter = ['Attendance_student_ID', 'status', 'date']
    search_fields = ['Attendance_student_ID', 'status', 'date']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)