from rest_framework.response import Response
from rest_framework import status
from.serializers import  LoggedInUserSerializer
from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from drf_yasg import openapi


    
"""
Implementing swagger api in function based view, asking for username and password in query param
"""
#This code is while I am learning Django authentication
@swagger_auto_schema(methods=['GET'] ,manual_parameters=[
    openapi.Parameter('username', openapi.IN_QUERY, type=openapi.TYPE_STRING , required=True),
    openapi.Parameter('password', openapi.IN_QUERY, type=openapi.TYPE_STRING , required=True)

    ])
@api_view(['GET'])
def login_user(request):
    if request.method == "GET":
        password = request.GET.get('password') # function base view [ Accessing query params ]
        username = request.GET.get('username')

        user = authenticate(username=username, password=password)

        if user is not None:
            success_message = {
                "message":f"hi, {user.username} You are successfully logged in !"
            }
            return Response(success_message, status=status.HTTP_200_OK)
        
        error_message = {
                "message":f"password or username did not match"
            }
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)






"""
Implementing swagger api in function based view, asking for username and password in request body
"""
@swagger_auto_schema(methods=["POST"],
                     request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['username', 'password'],
    properties={
        "username": openapi.Schema(type=openapi.TYPE_STRING),
        "password": openapi.Schema(type=openapi.TYPE_STRING)
    },
    example={
        "username": "Sita",
        "password": "Sita@123"
    }
    )
)

@api_view(['POST'])
def login_userv2(request):
    if request.method == "POST":

        username = request.data.get('username') # function base view [ Accessing request data ]
        print("***************username from request is => ", username)
        serializer = LoggedInUserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

            if user is not None:
                login(request, user)
                success_message = {
                    "message": f"Hi, {user.username}! You are successfully logged in!"
                }
                return Response(success_message, status=status.HTTP_200_OK)
            error_message = {
                    "message": "Invalid username or password"
                }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




