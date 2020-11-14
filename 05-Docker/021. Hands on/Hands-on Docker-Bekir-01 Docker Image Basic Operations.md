# Hands-on Docker-Bekir-01 : Docker Image Basic Operations

## Part 1 - Building Docker Images with Dockerfile

- Build an image of Dockerfile based on `alpine` image and push it to the Docker Hub.

- Create a folder to hold all files necessary for creating Docker image.

```bash
cd ~
mkdir MyFirstImage
cd MyFirstImage
```

- Create a Dockerfile listing necessary packages and modules, and name it `Dockerfile`
  
```bash
echo '
FROM alpine:latest
CMD ["ping", "-c","5", "google.com"]
' > Dockerfile
```


- Build Docker image from Dockerfile locally, tag it as `<Your_Docker_Hub_Account_Name>/<Your_Image_Name>:<Tag>` and explain steps of building. Note that repo name is the combination of `<Your_Docker_Hub_Account_Name>/<Your_Image_Name>`.

```bash
docker build -t "siberblog/pingtest:1.0" .
docker image ls
```


- Run the newly built image as container.

```bash
docker run --name myfirstcontainer siberblog/pingtest:1.0
docker ps -a
```


- Remove the newly built myfirstcontainer.

```bash
docker rm  myfirstcontainer
or 
docker rm a24bb4013296
docker ps -a
```


- Login in to Docker with credentials.

```bash
docker login
```


- Push newly built image to Docker Hub, and show the updated repo on Docker Hub.

```bash
docker push siberblog/pingtest:1.0
```


- Delete image with `image id` locally.

```bash
docker image rm siberblog/pingtest:1.0
or 
docker rmi siberblog/pingtest:1.0
```



## Part 2 - Building Docker Images with Dockerfile Version:2.0


```bash
cd ~
mkdir MySecondImage
cd MySecondImage
```

```bash
echo '
echo "Google ping Test:"
ping -c 5 google.com
' > googlePingTest.sh
```


```bash
echo '
FROM alpine
COPY googlePingTest.sh googlePingTest.sh
CMD ["sh", "googlePingTest.sh"]
' > Dockerfile
```


- Build Docker image from Dockerfile locally, tag it as `<Your_Docker_Hub_Account_Name>/<Your_Image_Name>:<Tag>` and explain steps of building. Note that repo name is the combination of `<Your_Docker_Hub_Account_Name>/<Your_Image_Name>`.

```bash
docker build -t "siberblog/pingtest:2.0" .
docker images
```


- Run the newly built image as container.

```bash
docker run --name mysecondcontainer siberblog/pingtest:2.0
docker ps -a
```


- Login in to Docker with credentials.

```bash
docker login
```


- Push newly built image to Docker Hub, and show the updated repo on Docker Hub.

```bash
docker push siberblog/pingtest:2.0
```


- Remove the newly built mysecondcontainer.

```bash
docker rm mysecondcontainer
or 
docker rm a24bb4013296
docker ps -a
```


- Delete image with `image id` locally.

```bash
docker image rm siberblog/pingtest:2.0
or 
docker rmi siberblog/pingtest:2.0
docker images -a
```
