
import subprocess
import shutil 

class DockerCommand:
    
    DOCKER = "docker"
    DOCKER_COMPOSE = "docker-compose"
    DOCKER_COMPOSE_UP = "up"
    DOCKER_COMPOSE_UP = "down"

    def run(self, artifact):
        dockerExecutable = shutil.which(DOCKER)
        if dockerExecutable is not None: 
          #checks if command line is available 
            dockerProcess = subprocess.Popen(DOCKER_COMPOSE_UP, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = dockerProcess.wait()
