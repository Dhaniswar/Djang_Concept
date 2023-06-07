from django.shortcuts import render
from rest_framework.views import APIView
from .models import Author, Blog, Entry
from .serializers import AuthorSerializer, BlogSerializer, EntrySerializer
from rest_framework import status
from rest_framework.response import Response


class AuthorAPIViewDetails(APIView):
    def get(self, request):
        queryset = Author.objects.exclude(name="Paul")
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

class BlogAPIViewDetails(APIView):
    
    def get(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EntryAPIViewDetails(APIView):
    
    def get(self, request):
        queryset = Entry.objects.all()
        serializer = EntrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)