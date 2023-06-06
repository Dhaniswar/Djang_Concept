from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address', 'email', 'section']
