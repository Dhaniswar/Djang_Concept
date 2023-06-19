from django.shortcuts import render

from authentication.functional_base_views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import CreateUserSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import Person, Student

from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


class CreateUserAPIView(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = CreateUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=CreateUserSerializer)
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomPermissionAPIView(APIView):
    def get(self, request):
        # content_type = ContentType.objects.all() # It display the all app name and respective model name in this format [ authentication | person]
        # for content in content_type:
        #     print("****** : ", content)
        

        """
        # if we pass Specific model to get_for_model(Person) method it display the specific aap name and model name like this
        ********* content_type :  authentication | person
        """
        content_type = ContentType.objects.get_for_model(Person) 
        print('********* content_type : ', content_type)

        person_permission = Permission.objects.filter(content_type=content_type) # this line return the queryset of all permission available to Person model
        permissions = [p.codename for p in person_permission] # this line display the list of permissions belongs to Person Model
        print("***********person permission : ", permissions)

        payload = {
            "permissions": permissions
        }

        return Response(payload, status=status.HTTP_200_OK)
    

    def post(self, request):
        """
        # if we pass Specific model to get_for_model(Person) method it display the specific aap name and model name like this
        ********* content_type :  authentication | person
        """
        content_type = ContentType.objects.get_for_model(Person) 
        permission = Permission.objects.create(
            codename = "can_buy_pizzas",
            name = "Can buy pizzas",
            content_type=content_type
        )

        print("***********person permission : ", permission)

        payload = {
            "permissions": "permissions Created"
        }

        return Response(payload, status=status.HTTP_201_CREATED)



class AddPermissionToUserApiView(APIView):

    def get(self, request):
        content_type = ContentType.objects.get_for_model(Person) 
        user = User.objects.get(pk=1)
        person_permission = Permission.objects.filter(content_type=content_type) # this line return the queryset of all permission available to Person model

        [user.user_permissions.add(permission) for permission in person_permission]

        payload = {
            "permissions": "successfully added permission to user"
        }

        return Response(payload, status=status.HTTP_200_OK)
