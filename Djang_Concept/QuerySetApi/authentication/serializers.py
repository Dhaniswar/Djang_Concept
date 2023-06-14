from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class CreateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["last_login", "date_joined"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        groups_data = validated_data.pop("groups", [])
        user_permissions_data = validated_data.pop("user_permissions", [])
        user= User(**validated_data)
        user.set_password(password)
        user.save()

         # Add groups to the user
        for group_data in groups_data:
            group_id = group_data.get("id")
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
        
        # Add user permissions to the user
        for permission_data in user_permissions_data:
            permission_id = permission_data.get("id")
            permission = Permission.objects.get(id=permission_id)
            user.user_permissions.add(permission)
        
        return user