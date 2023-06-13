from django.shortcuts import render
from rest_framework.views import APIView
from .models import Author, Blog, Entry
from .serializers import AuthorSerializer, BlogSerializer, EntrySerializer
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response

import datetime


class AuthorAPIViewDetails(APIView):
    def get(self, request):
        queryset = Author.objects.exclude(name="Paul")
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

class BlogAPIViewDetails(APIView):
    
    def get(self, request, pk):
        try:
            queryset = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
        serializer = BlogSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request):
        # queryset = Blog.objects.all()[1:6] # it exclude first argument and include last argument

        # queryset = Blog.objects.all()[-1] # Negative indexing is not supported

        # queryset = Blog.objects.all()[1::2] # display all records whose primary key or id is even

        # queryset = Blog.objects.all()[::2] # display all records whose primary key or id is odd

        # queryset = Blog.objects.order_by("name")[0] # if you want to retrieve one object use index ( use many=False in serializer)

        # queryset = Blog.objects.order_by("name")[0:1].get() if you want to retrieve one object use index ( use many=False in serializer)

        # queryset = Blog.objects.get(name__exact="Drinking Water") # for exact match use exact lookup

        """
        If error is Models object is not iterable then make sure serializers arguments many=False
        """
        # queryset = Blog.objects.filter(name__iexact="Drinking Water") # iexact lookup display matching all it is not case sensitive
        
        # queryset_id = Blog.objects.values_list('id', flat=True)[1::2] # displaying only even id
        # print("************ queryset_id : ", queryset_id)

      


        queryset = Blog.objects.all()


        serializer = BlogSerializer(queryset, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EntryAPIViewDetails(APIView):
    def get(self, request, pk):
        try:
            queryset = Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404
        serializer = EntrySerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request):
        # queryset = Entry.objects.filter(headline__startswith="What").exclude(pub_date__gte=datetime.datetime.today()).filter(pub_date__gte=datetime.date(2023, 6, 7))
        # queryset = Entry.objects.filter(headline__startswith="What")
        queryset = Entry.objects.all()
        serializer = EntrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)