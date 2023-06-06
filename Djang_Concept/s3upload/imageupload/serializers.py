# import serializer from rest_framework
from rest_framework import serializers

from .models import Image
class ImageSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Image
        fields = "__all__"
