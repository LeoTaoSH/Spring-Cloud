Build docker image
mvn clean
mvn package docker:build

docker run --name eureka-server -p 8761:8761 -t spring-cloud/spring_cloud_netflix_eureka
docker run --name eureka-client --link eureka-server:8761 -p 8763:8763 -t spring-cloud/spring_cloud_netflix_eureka_client

docker-compose up
docker-compose down

for bring up containers already built the images
docker-compose -f docker-compose.yml up

for build images and bring up containers
docker-compose -f docker-compose-dev.yml up