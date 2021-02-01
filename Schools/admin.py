from django.contrib import admin
from .models import School, Teacher, Student


# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_ID', 'school_name', 'school_street_address', 'school_city', 'school_state', 'school_zip']
    list_filter = ['school_ID', 'school_name', 'school_street_address', 'school_city', 'school_state', 'school_zip']
    search_fields = ['school_ID', 'school_name', 'school_street_address', 'school_city', 'school_state', 'school_zip']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_ID', 'school_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade',
                    'teacher_email', 'teacher_phone']
    list_filter = ['teacher_ID', 'school_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade',
                   'teacher_email', 'teacher_phone']
    search_fields = ['teacher_ID', 'school_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade',
                     'teacher_email', 'teacher_phone']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade', 'student_school_ID',
                    'student_teacher_ID']
    list_filter = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade', 'student_school_ID',
                   'student_teacher_ID']
    search_fields = ['student_ID', 'student_lastname', 'student_firstname', 'student_grade', 'student_school_ID',
                     'student_teacher_ID']


admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
