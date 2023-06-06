from django.shortcuts import render
from course_details.serializers import CourseSerializer
from course_details.models import Course
from custom_exception_handler.exceptions.exception import UnreadableCSVFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated





class CourseList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetails(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise UnreadableCSVFile()
    
    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = CourseSerializer(queryset, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = CourseSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        message = {
            "details": "Data is successfully deleted"
        }
        return Response(message, status=status.HTTP_204_NO_CONTENT)
