# Temperature_conversion 

## This is a repo for Cloud-computing course Project 2

## This simple docker container is a calculator to perform temperature conversion from celsius to fahrenheit or from fahrenheit to celsius.


## Run in container

```
docker build --tag=app .
## convert fahrenheit to celsius
docker run -it app python app.py --type 'F' --temp 98
## convert celsius to fahrenheit
docker run -it app python app.py --type 'C' --temp 36.66
## a wrong type of temperature
docker run -it app python app.py --type 'X' --temp 98
```

## Tags and Uploads an image to Docker Hub

```
chmod +x push_docker.sh && ./push_docker.sh
```
## Pull the image from Dockerhub

```
docker pull jingjingshi09/temp_conversion:latest
## convert fahrenheit to celsius
docker run -it jingjingshi09/temp_conversion python app.py --type 'F' --temp 98
## convert celsius to fahrenheit
docker run -it jingjingshi09/temp_conversion python app.py --type 'C' --temp 36.66
## a wrong type of temperature
docker run -it jingjingshi09/temp_conversion python app.py --type 'X' --temp 98
```
