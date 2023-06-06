from django.urls import path
from blog.views import home, BlogDetails, BlogList


urlpatterns = [
    path('home', home, name= 'home'),
    path('blog', BlogList.as_view(), name="Blog-List"),
    path('blog/<int:pk>', BlogDetails.as_view(), name="Blog-Details"),
]