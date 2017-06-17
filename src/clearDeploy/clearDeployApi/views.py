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
        return Response('Simple Deployer')

    def post(self, request, format=None):
        return Response('Simple Deployer')

    def put(self, request, format=None):
        return Response('Simple Deployer')

#  @api_view(['GET', 'PUT', 'DELETE'])
#  def view1(request, format=None):
#     execfile = shutil.which('terraform') 
#     if (execfile != None):
#         return Response('terraforming')

#     return Response('Nothing requested')

# @api_view(['GET', 'PUT', 'DELETE'])
# def view2(request):
#     return Response('MIKI LAI')

# @api_view(['POST'])
# def view3(request):
#     return Response('MIKI LAI')