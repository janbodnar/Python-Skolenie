# Docker

## Commands

`$ docker build -t myapp .` - build image from Dockerfile  
`$ docker tag myapp janbodnar/spring-boot-simple:first` - tag image  
`$ docker ps` - show running containers  
`$ docker image ls` - list Docker images  
`$ docker images` - list Docker images  
`$ docker pull devilbox/php-fpm-7.4` - pull image  
`$ docker image rm -f a084fe86889b` - remove image 
`$ docker rmi -f 90b1c3e39075`  - remove image  
`$ docker run -it --entrypoint /bin/bash <image id>` run shell in image  
`$ docker exec -it <container name> /bin/bash` - connect into container  
`$ docker cp hello.php infallible_bassi:/var/www/html` - copy file to container  
`$ docker run -p 127.0.0.1:80:8080/tcp ubuntu bash` - binds port 8080 of the container to 
TCP port 80 on 127.0.0.1 of the host machine  
`$ docker stop 03ccf5a72537` - stop running container  
`$ docker push janbodnar/spring-boot-simple:first`  - upload image to hub  
`$ docker pull janbodnar/spring-boot-simple:first`  - pull image from hub  

`$ docker run -it python:3.8 hostname -i`  -- find out IP address  

`# systemctl start docker` -- start docker  
`sudo systemctl enable docker` -- enable docker to star on boot  
`sudo usermod -aG docker $USER`  -- allow non-root user to run docker  

**prune dangling &lt;none&gt;:&lt;none&gt; images**  
`# docker image prune`  
`# docker rmi -f $(docker images -f "dangling=true" -q)`  
