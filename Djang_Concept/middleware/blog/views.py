from django.shortcuts import render, HttpResponse
from django.http import Http404
from blog.serializers import BlogSerializer
from blog.models import Blog
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class BlogList(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetails(APIView):

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = BlogSerializer(queryset, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = BlogSerializer(queryset, data=request.data)
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

def home(request):
    print("I am from view")
    return HttpResponse("This is home page")
