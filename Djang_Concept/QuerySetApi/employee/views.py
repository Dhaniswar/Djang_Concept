from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeListAPIViewSet(APIView):
    def get(self, request):
        queryset = Employee.objects.all().order_by('-created_at')
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=EmployeeSerializer)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmployeeDetailsAPIViewSet(APIView):

    def get_object(self,  pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
   
    def get(self, request, pk):
        employee = self.get_object(self, request, pk)
        serializer = EmployeeSerializer(employee, many=False)
        Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EmployeeSerializer)
    def put(self, request, pk):
        employee = self.get_object(self, pk)
        serializer = EmployeeSerializer(employee ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        employee = self.get_object(self, pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']