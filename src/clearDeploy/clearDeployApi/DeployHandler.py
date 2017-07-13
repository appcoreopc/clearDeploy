from clearDeployApi.models import DeploymentStatus, Artifact


class DeployHandler: 

    def startDeploy(self, artifactId):
        # update deployment status
        self.updateDeploymentStatus(artifactId)
        # get the type of deployment 
        self.getDeploymentInfo(artifactId)
    
    def getDeploymentInfo(self, artifactId):
        artifact = Artifact.objects.get(pk = artifactId)
        if artifact is not None: 
            artifactType = artifact.packageInfo
            if artifactType is not None: 
                if artifactType.artifactProviderName == "Docker":
                    # run docker 
                    print("runnng docker")
                elif artifactType.artifactProviderName == "Kurbenetes":
                    # run kurbenetes
                    print("running kurbenetes")
                elif artifactType.artifactProviderName == "AWS":
                    # run kurbenetes
                    print("running kurbenetes")


    def updateDeploymentStatus(self, artifactId, status = 1):
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
        