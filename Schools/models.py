from django.db import models


# Create your models here.
class School(models.Model):
    school_ID = models.CharField(primary_key=True, max_length=10, blank=False, null=False, default=' ')
    school_name = models.CharField(max_length=50, blank=False, null=True, default='')
    school_street_address = models.CharField(max_length=100, blank=False, null=True, default='')
    school_city = models.CharField(max_length=50, blank=False, null=True, default='')
    school_state = models.CharField(max_length=50, blank=False, null=True, default='')
    school_zip = models.CharField(max_length=50, blank=True, null=True, default='00000')

    def __str__(self):
        return str(self.school_name)


class Teacher(models.Model):
    teacher_ID = models.CharField(primary_key=True, max_length=10, blank=False, null=False, default=' ')
    teacher_lastname = models.CharField(max_length=50, blank=False, null=True, default='')
    teacher_firstname = models.CharField(max_length=50, blank=False, null=True, default='')
    teaching_grade = models.CharField(max_length=50, blank=False, null=True, default='')
    teacher_street_address = models.CharField(max_length=100, blank=False, null=True, default='')
    teacher_city = models.CharField(max_length=50, blank=False, null=True, default='')
    teacher_state = models.CharField(max_length=50, blank=False, null=True, default='')
    teacher_zip = models.CharField(max_length=50, blank=True, null=True, default='00000')
    teacher_email = models.EmailField(max_length=100, default=' ')
    teacher_phone = models.CharField(max_length=50, default='(402)000-0000')
    school_ID = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school')

    def __str__(self):
        return str(self.teacher_firstname)


class Student(models.Model):
    student_ID = models.CharField(primary_key=True, max_length=10, blank=False, null=False, default=' ')
    student_lastname = models.CharField(max_length=50, blank=False, null=True, default='')
    student_firstname = models.CharField(max_length=50, blank=False, null=True, default='')
    student_grade = models.CharField(max_length=50, blank=False, null=True, default='')
    student_school_ID = models.ForeignKey(School, on_delete=models.CASCADE, related_name='School')
    student_teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Teacher')

    def __str__(self):
        return str(self.student_firstname)