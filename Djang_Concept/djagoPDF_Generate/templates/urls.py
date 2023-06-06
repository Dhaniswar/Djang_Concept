from django.urls import path

#This will import our view that we have already created
from .views import GeneratePdf

urlpatterns = [
    path('', GeneratePdf.as_view()), 
]