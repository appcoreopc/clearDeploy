# python manage.py migrate --run-syncdb

from django.db import models
from django.utils import timezone

# Create your models here.
class PackageInfo(models.Model):
    version = models.TextField()
    artifactProviderName = models.TextField()
    description = models.TextField()

    def __init__(self, **kwargs):
        self.version = kwargs['version']
        self.delete = kwargs['description']

class Artifact(models.Model):
    description = models.TextField()
    version = models.TextField()
    packagePath = models.TextField()
    dateCreated = models.DateTimeField()
    dateDeployed = models.DateTimeField()
    packageInfo = models.ForeignKey(PackageInfo)

    def __init__(self, **kwargs):
        self.description = kwargs['description']
        self.version = kwargs['version']

    def __str__(self):
        return self.description

    def deploy(self):
        self.date = timezone.now()
        self.save()

class Project(models.Model):
    Name = models.TextField()
    Artifacts = models.ForeignKey(Artifact)
    Active = models.NullBooleanField()

class AppUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    dateCreate = models.DateField()

    def create(self):
        self.save()
    
class DeployHistory(models.Model):
     description = models.TextField()
     dateCreated = models.DateTimeField()
         