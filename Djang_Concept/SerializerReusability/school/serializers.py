from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        if hidden_fields := self.context.get('hidden_fields', None):
            for field in hidden_fields:
                if field in fields:
                    fields.pop(field)
        return fields





