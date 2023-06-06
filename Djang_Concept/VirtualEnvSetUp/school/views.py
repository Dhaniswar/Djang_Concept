from rest_framework import viewsets

from .models import Student, Teacher
from .serializers import StudentSerializer


class StudentDetails(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


