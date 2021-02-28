from django import forms
from .models import Student, Teacher, Attendance


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_ID', 'student_lastname', 'student_firstname', 'student_grade', 'teacher')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('teacher_ID', 'teacher_lastname', 'teacher_firstname', 'teaching_grade', 'teacher_email', 'teacher_phone')


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('student', 'status')
