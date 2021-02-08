from django import forms
from .models import Student, Teacher


class CreateStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_ID', 'student_lastname', 'student_firstname', 'student_grade', 'student_teacher_ID')


class CreateTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('teacher_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade',
                 'teacher_email', 'teacher_phone')
