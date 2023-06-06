from django.urls import path
from .views import ImageAPIView

urlpatterns = [
	path('', ImageAPIView.as_view(), name = 'image_api_view'),
]
