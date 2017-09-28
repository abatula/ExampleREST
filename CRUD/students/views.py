from .models import Student
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import StudentSerializer


def index(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'students/index.html', context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
