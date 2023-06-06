from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StudentDetails


router = DefaultRouter()
router.register('api',StudentDetails)

urlpatterns = [
    path('', include(router.urls)),
   
]



# urlpatterns = [
#     path('api/',StudentDetails.as_view({'get':'list','post':'create'}), name="Student-Details"),
#     path('api/<int:pk>/',StudentDetails.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="Student-Details"),
# ]
