from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db import models
from clearDeployApi.models import AppUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    #language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    #style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    class Meta:
        ordering = ('created',)

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos')

class AppUserSerializer(serializers.ModelSerializer):
   class Meta:
     model = AppUser
     fields = ('id', 'username', 'password', 'dateCreate')

class AppsUserSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=AppUserSerializer())
    class Meta:
     model = AppUser
     fields = ('items')
