# Docker get-starter
this is for docker experiment [docker-starter](https://docs.docker.com/get-started/) and docker swarm usage
# 1), Orientation
- List Docker CLI commands
```
docker
docker container --help
```

- Display Docker version and info
```
docker --version
docker version
docker info
```
- Execute Docker image
```
docker run hello-world
```
- List Docker images
```
docker image ls
```
- List Docker containers (running, all, all in quiet mode)
```
docker container ls
docker container ls --all
docker container ls -aq
```

# 2), Containers 
- Create image using this directory's Dockerfile
```
docker build -t friendlyhello . 
```

- Run "friendlyname" mapping port 4000 to 80
```
docker run -p 4000:80 friendlyhello
```
- Same thing, but in detached mode
```
docker run -d -p 4000:80 friendlyhello
```

- List all running containers
```
docker container ls
```

- List all containers, even those not running
```
docker container ls -a
```

- Gracefully stop the specified container
```
docker container stop <hash>
```

- Force shutdown of the specified container
```
docker container kill <hash>
```

- Remove specified container from this machine
```
docker container rm <hash>
```

- Remove all containers
```
docker container rm $(docker container ls -a -q)
```

- List all images on this machine
```
docker image ls -a
```

- Remove specified image from this machine
```
docker image rm <image id>
```

- Remove all images from this machine
```
docker image rm $(docker image ls -a -q)
```

- Log in this CLI session using your Docker credentials
```
docker login --> use docker hub id(leotao/...)
```

- Tag <image> for upload to registry
```
docker tag <image> username/repository:tag
docker tag friendlyhello leotao/get-started:part2
```

- Upload tagged image to registry
```
docker push username/repository:tag
docker push leotao/get-started:part2
```

- Run image from a registry
```
docker run username/repository:tag
docker run -p 4000:80 leotao/get-started:part2
```

# 3), Services
- List stacks or apps
```
docker stack ls
```

- Run the specified Compose file, If you don’t run docker swarm init you get an error that “this node is not a swarm manager.”
```
docker swarm init
docker stack deploy -c <composefile> <appname>
```

- List running services associated with an app
```
docker service ls
```

- List tasks associated with an app
```
docker service ps <service>
```

- Inspect task or container
```
docker inspect <task or container>
```

- List container IDs
```
docker container ls -q
```

- Tear down an application
```
docker stack rm <appname>
```

- Take down a single node swarm from the manager
```
docker swarm leave --force
```



