
import subprocess, os 
import shutil 

class DockerCommand:

    DOCKER = "docker"
    DOCKER_COMPOSE = "docker-compose"
    DOCKER_COMPOSE_UP = "up"
    DOCKER_COMPOSE_DOWN = "down"

    def run(self, artifact):
        dockerExecutable = shutil.which(self.DOCKER)
        if dockerExecutable is not None: 
            try:    
                print(artifact.packagePath)
                os.chdir(artifact.packagePath)
                cmdParam = [self.DOCKER_COMPOSE, self.DOCKER_COMPOSE_UP]
                print(self.DOCKER_COMPOSE)
                print(self.DOCKER_COMPOSE_UP)
                dockerProcess = subprocess.call(cmdParam)
                #result = dockerProcess.wait()
                if dockerProcess == 0: 
                        print("program executed successfully.")   
            except ValueError as e: 
                        print("ops.. " + str(e))
            