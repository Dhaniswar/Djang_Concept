from django.urls import path

from employee.views import EmployeeListAPIViewSet, EmployeeDetailsAPIViewSet




urlpatterns = [
    path('', EmployeeListAPIViewSet.as_view(), name= "employee_list_api_view"),
    path('<int:pk>/', EmployeeDetailsAPIViewSet.as_view(), name= "employee_details_api_view")

]