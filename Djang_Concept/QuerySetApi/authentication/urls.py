from django.urls import path
from .views import CreateUserAPIView, CustomPermissionAPIView, AddPermissionToUserApiView, login_user, login_userv2


urlpatterns = [
    path('', CreateUserAPIView.as_view(), name="create-user-api-view"),
    path('custom-permission/', CustomPermissionAPIView.as_view(), name="custom-permission-api-view"),
    path('add-permission-to-user/', AddPermissionToUserApiView.as_view(), name="add-permission-to-user"),
    path('login/', login_user, name="login-user"),
    path('login/v2/', login_userv2, name="login-user-v2"),

]