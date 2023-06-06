from rest_framework import serializers

from userdetails.models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = "__all__"