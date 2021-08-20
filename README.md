# Run lazypredict in a docker container
This small project shows how to run [lazypredict](https://lazypredict.readthedocs.io/en/latest/readme.html#installation) in docker container. Some of the dependencies may conflict with tensorflow installation. Thus, this seemed to me the right approach as lazypredict is just a nice first step towards the development of your own machine learning models. This way, as I have tensorflow physically installed in my computer, **there is no need to install lazypredict, locally, in your machine**, and mess all your other python packages. In this [link](https://towardsdatascience.com/build-and-run-a-docker-container-for-your-machine-learning-model-60209c2d7a7f), you can read more about the advantages of running your machine learning models in docker containers.

# Overview

> Lazy Predict helps build a lot of basic models without much code and helps understand which models works better without any parameter tuning.


# Docker installation

To create and use docker containers you must first install docker on your computer. You can check it how, here in this [post](https://xaviervasques.medium.com/quick-install-and-first-use-of-docker-327e88ef88c7). Beware docker needs sudo permissions. You may use ```sudo``` command before using ```docker``` command, or you mays follow these steps in [docker documentation](https://docs.docker.com/engine/install/linux-postinstall/).


# Building Dockerfile
We are now ready to start building our own containers! Open a terminal window and go to your folder where Dockerfile is, for instance:

```
>>> cd ~/workspace/projects/lazy-app
```
For this project we will build our docker image from our Dockerfile. Thus, we use the following command:

```
docker build -t [image tag] .
```
or 
```
docker build -t [image tag] -f Dockerfile .
```
Example:
```
docker build -t lazy .
```
If we run ```docker images```in our terminal, we will list all the images that are present in our computer, and of course, our recently built docker image, named lazy, will be there.


# Running docker image

After creating the docker image, it is time to create and run a docker container to start trainning some models! We want to see the output, that is why we will run our container in interactive mode by using -it options.

 > Run a container with no options and by default you have a stdout stream (so docker run | <cmd> works); run with -i, and you get stdin stream added (so <cmd> | docker run -i works)

 With ```-it``` you have a terminal driver added. It basically makes the container start look like a terminal connection session.

```
docker run -it --name [container name] [image tag]
```

Example:
```
docker run -it --name lazyc lazy
```

You may also list all the available containers using the following:

```
docker ps -a
```

**NOTE**: to remove an image you must first remove the container. You can achieve that by using
```
> docker rm [container's name or ID]

> docker image rm [image name or ID]
```

# Conclusion
Here we provide an easy way for you to start exploring the right models for your applications without the need of preparing any virtual environment or installing any packages in your local file system. Just put your dataset file in the data folder and you are go to go :relaxed: 
 