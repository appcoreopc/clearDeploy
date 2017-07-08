from clearDeployApi.models import DeploymentStatus

class DeployHandler: 
    def startDeploy(self, artifactId):
        self.updateDeploymentStatus(artifactId)
        

        
    def updateDeploymentStatus(self, artifactId):
        if artifactId == -1:
            ds = DeploymentStatus()
            ds.deployer = "Default"
            ds.deploymentId = artifactId
            ds.description = "Test"
            ds.status = 1
            ds.version = "1"
            ds.save()
        else:
            ds = DeploymentStatus.objects.get(id=artifactId)
            ds.status = 1
            ds.save()
        