"""clearDeploy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from clearDeployApi import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^/test/product/', views.view1),
    #url(r'^/test/product/search/', views.view2),
    url(r'^$', views.api_root),
    url(r'^artifacts/$', views.ProjectArtifact.as_view(), name='artifact-list'),
    url(r'^artifacts/(?P<appId>\d+)/$', views.ProjectArtifact.get),
    url(r'^deploy/$', views.SimpleDeployer.as_view(), name='deploy-list'),
    url(r'^deploy/simple/$', views.SimpleDeployer.as_view(), name='simple-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)