from rest_framework import viewsets
from .models import Student
from .serializers import  StudentSerializer


class StudentDetails(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']