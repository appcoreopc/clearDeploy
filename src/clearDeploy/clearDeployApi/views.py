from shutil import which
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.core import serializers
from clearDeployApi.DeployHandler import DeployHandler
from clearDeployApi.serializers import UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import renderers
from rest_framework.reverse import reverse
from clearDeployApi.models import AppUser, Project, Artifact
from clearDeployApi.serializers import AppUserSerializer, AppsUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# For our root API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'deploy': reverse('deploy-list', request=request, format=format),
        'simple': reverse('simple-list', request=request, format=format),
        'artifacts': reverse('artifact-list', request=request, format=format),
    })

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
     Deployer 
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

    # Create a deployment
    def post(self, request, format=None):
        # Update deployment status table
        # Run deployment scripts 
        # CleanUp
        id = request.data['Id']
        deployer = DeployHandler()
        deployer.startDeploy(id)
        return Response('POST Simple Deployer')

    def put(self, request, format=None):
        return Response('PUT Simple Deployer')

# 
class ProjectArtifact(APIView):
    """
     Rest for project artifact
    """
    def get(self, appId):
        if appId != None:
            try:
                result = Project.objects.get(id=int(appId))
                response = serializers.serialize('json', [result])
                return JsonResponse(response, status=200, safe=False)
            except Exception as e:
                return JsonResponse(str(e), status=509, safe=False)
    
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


class SnippetHighlight(generics.GenericAPIView):
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        #snippet = self.get_object()
        return Response("test")
