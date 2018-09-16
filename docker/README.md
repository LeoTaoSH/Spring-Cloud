#Docker get-starter
this is for docker experiment [docker-starter](https://docs.docker.com/get-started/)
#1), Orientation
- List Docker CLI commands
docker
docker container --help

- Display Docker version and info
docker --version
docker version
docker info

- Execute Docker image
docker run hello-world

- List Docker images
docker image ls

- List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq

#2), Containers
docker build -t friendlyhello .  
## Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello  
## Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         
## Same thing, but in detached mode
docker container ls                                
## List all running containers
docker container ls -a             
## List all containers, even those not running
docker container stop <hash>           
## Gracefully stop the specified container
docker container kill <hash>         
## Force shutdown of the specified container
docker container rm <hash>        
## Remove specified container from this machine
docker container rm $(docker container ls -a -q)         
## Remove all containers
docker image ls -a                             
## List all images on this machine
docker image rm <image id>            
## Remove specified image from this machine
docker image rm $(docker image ls -a -q)   
## Remove all images from this machine
docker login --> use docker hub id(leotao/...)            
## Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  --> docker tag friendlyhello leotao/get-started:part2
## Tag <image> for upload to registry
docker push username/repository:tag --> docker push leotao/get-started:part2
## Upload tagged image to registry
docker run username/repository:tag --> docker run -p 4000:80 leotao/get-started:part2                   
## Run image from a registry

3), Services
docker stack ls                                            
## List stacks or apps
docker swarm init
docker stack deploy -c <composefile> <appname>  
## Run the specified Compose file
docker service ls                 
## List running services associated with an app
docker service ps <service>                  
## List tasks associated with an app
docker inspect <task or container>                   
## Inspect task or container
docker container ls -q                                      
## List container IDs
docker stack rm <appname>                             
## Tear down an application
docker swarm leave --force      
## Take down a single node swarm from the manager
If you don’t run docker swarm init you get an error that “this node is not a swarm manager.”

#4), Swarms
docker swarm init to enable swarm mode and make your current machine a swarm manager.then run docker swarm join on other machines to have them join the swarm as workers. 
docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2
docker-machine ls
create and init docker swarm manager by execute below command, docker swarm init.
docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip>" --> docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100"
add a myvm2 as worker:
Always run docker swarm init and docker swarm join with port 2377 (the swarm management port), or no port at all and let it take the default. get the join token: docker-machine ssh myvm1 "docker swarm join-token -q worker"
docker-machine ssh myvm2 "docker swarm join --token SWMTKN-1-4d44q912a1ezr3guxcer2j40m7zxv4p03251zoyo5burkdlr66-65iqg16kfdkpuvrehdfl1gb9g 192.168.99.100:2377"
docker-machine ssh myvm1 "docker node ls"


docker-machine create --driver virtualbox myvm1 
## Create a VM (Mac, Win7, Linux)
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1 
## Win10
docker-machine env myvm1                
## View basic information about your node
docker-machine ssh myvm1 "docker node ls"         
## List the nodes in your swarm
docker-machine ssh myvm1 "docker node inspect <node ID>"        
## Inspect a node
docker-machine ssh myvm1 "docker swarm join-token -q worker"   
## View join token
docker-machine ssh myvm1   
## Open an SSH session with the VM; type "exit" to end
docker node ls                
## View nodes in swarm (while logged on to manager)
docker-machine ssh myvm2 "docker swarm leave"  
## Make the worker leave the swarm
docker-machine ssh myvm1 "docker swarm leave -f" 
## Make master leave, kill swarm
docker-machine ls 
## list VMs, asterisk shows which VM this shell is talking to
docker-machine start myvm1            
## Start a VM that is currently not running
docker-machine env myvm1      
## show environment variables and command for myvm1
eval $(docker-machine env myvm1)         
## Mac command to connect shell to myvm1
& "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression   
## Windows command to connect shell to myvm1
docker stack deploy -c <file> <app>
## Deploy an app; command shell must be set to talk to manager (myvm1), uses local Compose file
docker-machine scp docker-compose.yml myvm1:~ 
## Copy file to node's home dir (only required if you use ssh to connect to manager and deploy the app)
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"   
## Deploy an app using ssh (you must have first copied the Compose file to myvm1)
eval $(docker-machine env -u)
## Disconnect shell from VMs, use native docker
docker-machine stop $(docker-machine ls -q)               
## Stop all running VMs
docker-machine rm $(docker-machine ls -q) 
## Delete all VMs and their disk images

#5), Stacks
##add a new service: docker-compose-visualizer.yml
eval $(docker-machine env myvm1)
docker stack deploy -c docker-compose-visualizer.yml getstartedlab
docker-machine ls
##Open 192.168.0.101:8080
docker stack ps getstartedlab
##Presist data docker-compose-redis.yml,Create a ./data directory on the manager:
docker-machine ssh myvm1 "mkdir ./data"
eval $(docker-machine env myvm1)
docker stack deploy -c docker-compose-redis.yml getstartedlab
docker service ls
##Open 192.168.0.101:8080 dashboard


#6), Deploy your app
