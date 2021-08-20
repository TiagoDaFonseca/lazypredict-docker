# Run lazypredict in a docker container
This small project shows how to run lazypredict in docker container. Some of the dependencies may conflict with tensorflow installation. Thus, this seemed to me the right approach as lazypredict is just a first step towards the development of your own machine learning models. This way, as I have tensorflow physically installed in my computer, **there is no need to install lazypredict, locally, in your machine**.

# Overview

sdagagas

# Docker installation

To create and use docker containers you must first install docker on your computer. Here is how:


# Building Dockerfile

For this project we will build our docker image from our Dockerfile.

```
docker build -t [image tag] .
```
Example:
```
docker build -t lazyi
```

# Running docker image

```
docker run -it --name [container name] [image tag]
```

Example:
```
docker run -it --name lazyc lazyi
```

# Conclusion