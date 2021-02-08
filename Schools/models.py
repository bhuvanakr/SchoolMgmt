from django.db import models


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

    def __str__(self):
        return str(self.teacher_firstname)

    def __str__(self):
        return str(self.teacher_lastname)

    def __str__(self):
        return str(self.teaching_grade)


class Student(models.Model):
    student_ID = models.CharField(primary_key=True, max_length=10, blank=False, null=False, default=' ')
    student_lastname = models.CharField(max_length=50, blank=False, null=True, default='')
    student_firstname = models.CharField(max_length=50, blank=False, null=True, default='')
    student_grade = models.CharField(max_length=50, blank=False, null=True, default='')
    student_teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Teacher')

    def __str__(self):
        return str(self.student_firstname)

    def __str__(self):
        return str(self.student_lastname)

    def __str__(self):
        return str(self.student_grade)


class Attendance(models.Model):
    Attendance_student_ID = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Student')
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.status)
