# docker_project

## Create a local python virtual environment and source it 

```
python3 -m venv ~/.dockerproj
source ~/.dockerproj/bin/activate
```

## Install hadolint and other packages
(you may want to become root ```sudo wu -``` and then exit by typing ```exit```

```
wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.17.5/hadolint-Linux-x86_64 &&\
                chmod +x /bin/hadolint
pip install -r requirements.txt
```

## Run in container

```
docker build --tag=app .
docker run -it app bash
```

## Test app in shell

```
python app.py
```

## Tags and Uploads an image to Docker Hub

```
chmod +x push-docker.sh && ./push-docker.sh
```
