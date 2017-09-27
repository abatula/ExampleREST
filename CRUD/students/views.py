from .models import Student
from django.shortcuts import render, get_object_or_404


def index(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'students/index.html', context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})
