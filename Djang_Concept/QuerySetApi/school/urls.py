from django.urls import include, path
# from rest_framework.routers import DefaultRouter

from .views import  TeacherDetails

""""
router = DefaultRouter()
router.register('api',StudentDetails)

urlpatterns = [
    path('', include(router.urls)),
   
]
"""


urlpatterns = [
    # path('student/api/',StudentDetails.as_view({'get':'list','post':'create'}), name="Student-Details"),
    # path('student/api/<int:pk>/',StudentDetails.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="Student-Details"),
    path('teacher/api/',TeacherDetails.as_view({'get':'list','post':'create'}), name="Student-Details"),
    path('teacher/api/<int:pk>/',TeacherDetails.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="Student-Details"),


]
