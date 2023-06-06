
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student, Teacher
from .serializers import StudentSerializer


class StudentDetails(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request):
        object = Student.objects.all()
        serializer = StudentSerializer(object, many=True, context={'request': request,'hidden_fields': ['name', "roll", "city"]})
        return Response(serializer.data)
    