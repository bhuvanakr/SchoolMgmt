# from django.contrib.auth import models
from django.shortcuts import get_object_or_404
# from .models import Student, Teacher, Attendance
from django.utils import timezone

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
import sys


# Create your views here.
def home(request):
    return render(request, 'Schools/home.html', {'Schools': home})


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
    teachers = Teacher.objects.all()
    return render(request, "Schools/teacher_list.html", {'teachers': teachers})


@login_required
def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            teachers = Teacher.objects.all()
            return render(request, 'Schools/teacher_list.html',
                          {'teachers': teachers})
    else:
        form = TeacherForm()
    return render(request, "Schools/teacher_create.html", {'form': form})


@login_required
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            teachers = Teacher.objects.all()
            return render(request, 'Schools/teacher_list.html', {'teachers': teachers})

    else:
        form = TeacherForm(instance=teacher)
        return render(request, "Schools/teacher_edit.html", {'forms': form})


@login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('Schools:teacher_list')


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "Schools/student_list.html", {'students': students})


@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            students = Student.objects.all()
            return render(request, 'Schools/student_list.html',
                          {'students': students})
    else:
        form = StudentForm()

    return render(request, "Schools/student_create.html", {'forms': form})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            students = Student.objects.all()
            return render(request, 'Schools/student_list.html', {'students': students})
    else:
        form = StudentForm(instance=student)
    return render(request, "Schools/student_edit.html", {'form': form})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("Schools:student_list")


@login_required
def attendance_list(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Attendance.objects.filter(date__range=[fromdate, todate])
        return render(request, "Schools/attendance_list.html", {'attendances': searchresult})
    else:
        attendances = Attendance.objects.all()
        return render(request, "Schools/attendance_list.html", {'attendances': attendances})


@login_required
def attendance_create(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)

        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.save()
            attendances = Attendance.objects.all()
            return render(request, 'Schools/attendance_list.html',
                          {'attendances': attendances})
    else:
        form = AttendanceForm()

    return render(request, "Schools/attendance_create.html", {'forms': form})


@login_required
def attendance_edit(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendance)

        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.save()
            attendances = Attendance.objects.all()
            return render(request, 'Schools/attendance_list.html', {'attendances': attendances})
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, "Schools/attendance_edit.html", {'form': form})


@login_required
def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    attendance.delete()
    return redirect("Schools:attendance_list")
