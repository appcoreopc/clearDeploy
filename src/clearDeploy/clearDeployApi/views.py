from shutil import which
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from clearDeployApi.serializers import UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import renderers
from rest_framework.reverse import reverse
from clearDeployApi.models import AppUser
from clearDeployApi.serializers import AppUserSerializer, AppsUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SimpleDeployer(APIView):
    """
     Deploye 
    """

    def get(self, request, format=None):
        result = AppUser.objects.all()
        if result is not None:
            #return Response(AppUserSerializer(result[0]))
            #jsonResult = AppsUserSerializer(result)
            #return Response(jsonResult.data)
            jsonResult = AppUserSerializer(list(result), many=True)
            return Response(jsonResult.data)
            #return Response(AppUserSerializer(result[0]).data)
            #return Response('GET Simple Deployer22222')
        return Response('GET Simple Deployer')

    def post(self, request, format=None):
        return Response('POST Simple Deployer')

    def put(self, request, format=None):
        return Response('PUT Simple Deployer')


class AccessKey(generics.GenericAPIView):
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, format=None):
        return Response('Access  Key')

    def post(self, request, format=None):
        return Response('Access  Key')

    def put(self, request, format=None):
        return Response('Access  Key')

# For our root API

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'deploy': reverse('deploy-list', request=request, format=format),
        'simple': reverse('simple-list', request=request, format=format)
    })


class SnippetHighlight(generics.GenericAPIView):
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        #snippet = self.get_object()
        return Response("test")
