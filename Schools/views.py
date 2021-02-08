# from django.contrib.auth import models
from django.shortcuts import get_object_or_404
# from .models import Student, Teacher, Attendance
from .forms import *
from django.contrib import messages
# from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import *
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'schools/home.html', {'schools': home})


def logout(request):
    auth_logout(request)
    return redirect('/home')


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # logger.info("123")
                return redirect('/home')

    form = AuthenticationForm(request)
    return render(request, 'registration/login.html', {'form': form})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def teacher_list(request):
    teacher = Teacher.objects.all()
    return render(request, "schools/teacher_list.html", {'teachers': 'teacher'})


@login_required
def create_teacher(request):
    if request.method == "POST":
        form = CreateTeacher(request.POST)

        if form.is_valid():
            teacher = form.save(commit=False)
            messages.success(request, "Teacher Registration Successfully!")
            teachers = Teacher.objects.all()
            return render(request, 'schools/teacher_list.html',
                          {'teachers': teacher})
    else:
        form = CreateTeacher()

    return render(request, "schools/teacher_create.html", {'form': 'form'})


@login_required
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, teacher_ID=pk)

    if request.method == "POST":
        form = CreateTeacher(request.POST, instance=teacher)

        if form.is_valid():
            teacher = form.save()
            messages.success(request, "Edit Teacher Info Successfully!")
            teachers = Teacher.objects.all()
            return render(request, 'schools/teacher_edit.html', {'teachers': teachers})

    else:
        form = CreateTeacher(instance=teacher)
        return render(request, "schools/teacher_edit.html", {'teachers': teacher})


@login_required
def delete_teacher(request, teacher_id):
    teacher_delete = get_object_or_404(Teacher, id=teacher_id)
    teacher_delete.delete()
    messages.success(request, "Delete Teacher Info Successfully")
    return redirect('schools:teacher_list')


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "schools/student_list.html", {'students': 'student'})


@login_required
def create_student(request):
    if request.method == "POST":
        form = CreateStudent(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            messages.success(request, "Student Registration Successfully!")
            students = Student.objects.all()
            return render(request, 'schools/student_list.html',
                          {'students': students})
    else:
        form = CreateStudent()
        return render(request, "schools/student_create.html", {'forms': 'form'})


@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == "POST":
        form = CreateStudent(request.POST, instance=student)

        if form.is_valid():
            student = form.save()
            student.save()
            messages.success(request, "Edit Student Info Successfully!")
            students = Student.objects.all()
            return render(request, 'schools/student_list.html', {'students': students})
    else:
        form = CreateStudent(instance=student)
    return render(request, "schools/student_edit.html", {'form': 'form'})


@login_required
def delete_student(request, student_id):
    student_delete = get_object_or_404(Student, id=student_id)
    student_delete.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect("schools:student_list")


'''def attendance_count(request):
    grade = request.GET.get("grade", None)
    if grade:
        students = Student.objects.filter(Student, grade=student_grade)
        context = {"student_list": student_list}
    else:
        context = {}
    return render(request, "schools/attendance_count.html", context)'''

'''class AttendanceManager(models.Model):
    def create_attendance(self, student_grade, student_id):
        student_obj = Student.objects.get(
            class_type__class_short_form=student_grade,
            admission_id=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj'''

'''class Attendance(models.Model):
    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.admission_id'''
