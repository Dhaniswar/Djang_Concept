from rest_framework import serializers

from .models import  Teacher
import json

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ["id","name"]

    

#     def get_fields(self, *args, **kwargs):
#         print("inside get fields of serializer")
#         fields = super().get_fields(*args, **kwargs)
        

#         print("self.context is", self.context)

#         if hidden_fields := self.context.get('hidden_fields', None):
#             print("*******hidden_fields******", hidden_fields)

#             for field in hidden_fields:
#                 if field in fields:
#                     fields.pop(field)
#         print("*******Fields******", fields)
#         return fields


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        



