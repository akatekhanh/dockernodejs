import docker

class DockerControl:
    client = docker.from_env()
    
    # Parameter: 
        # image_name(str) : name of image
        # command(str): command when start the container
    def run_container(self,image_name,command=''):
        container = self.client.containers.run(image_name,command="",ports={'8081/tcp':4000})

    # Parameter: containerInfor(str) : name or Id of the container
    # Return a container object
    def get_container(self,containerInfor):
        try:
            return self.client.containers.get(containerInfor)
        except:
            raise docker.error.NotFound
    
    # Parameter: 
        # name(str): name or ID of the container which you want to stop
    def stop_container(self, name=""):
        for container in self.client.containers.list():
            if container.name == name or container.id in name:
                container.stop()
        

    

