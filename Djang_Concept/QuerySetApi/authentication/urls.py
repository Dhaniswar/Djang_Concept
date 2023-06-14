from django.urls import path
from .views import CreateUserAPIView


urlpatterns = [
    path('', CreateUserAPIView.as_view(), name="create-user-api-view"),
]