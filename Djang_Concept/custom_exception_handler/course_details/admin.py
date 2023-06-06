from django.contrib import admin
from course_details.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_id', 'duration', 'name', 'fees']

 
