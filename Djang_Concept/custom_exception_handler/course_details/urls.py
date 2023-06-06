from django.contrib import admin
from django.urls import path
from django.conf import settings
from course_details.views import CourseList, CourseDetails

urlpatterns = [
    path('', CourseList.as_view(), name="Course-List"),
    path('<int:pk>', CourseDetails.as_view(), name="Course-Details"),
]