from rest_framework.serializers import ModelSerializer
from .models import Author, Entry, Blog


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class EntrySerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = "__all__"


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"
        