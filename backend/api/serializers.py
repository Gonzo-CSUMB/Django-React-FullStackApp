from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"] # serialize only these fields
        extra_kwargs = {"password": {"write_only": True}} # don't serialize password, only use it for deserialization

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # create a user with the validated data
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"] # serialize only these fields
        extra_kwargs = {"author": {"read_only": True}}
        read_only_fields = ["author"] # don't allow the user to change the author
        