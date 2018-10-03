from django.contrib.auth.models import User
from rest_framework import serializers, views
from rest_framework.parsers import FileUploadParser

from beat_api.quickstart.models import File


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('file', 'name', 'price', 'artist', 'timestamp')
