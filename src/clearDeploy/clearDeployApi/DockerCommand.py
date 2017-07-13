
import subprocess
import shutil 

class DockerCommand:
    
    DOCKER_RUN = "docker run"
    DOCKER_COMPOSE_UP = "docker-compose up"
    DOCKER_COMPOSE_UP = "docker-compose down"

    def run(self, artifact):
        shutil.which(DOCKER_RUN)
        #checks if command line is available 
        dockerProcess = subprocess.Popen(DOCKER_COMPOSE_UP, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = dockerProcess.wait()
