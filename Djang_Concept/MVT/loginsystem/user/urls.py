from django.urls import path
from user.views import index
from django.conf.urls.static import static

urlpatterns = [
		path('', index, name ='index'),
]
