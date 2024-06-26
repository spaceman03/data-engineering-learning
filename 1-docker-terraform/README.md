# Week 1: Docker & Postgre SQL

## Introduction to Docker

### Simple docker pipeline example
With the [Dockerfile](2_docker_sql/Dockerfile) and [pipeline script](2_docker_sql/pipeline.py) in this directory, build and run the container with the following commands.

*Note: Run the Docker application before running the build image command in the terminal.*

**Step 1: Build the image**

```bash
docker build -t test:pandas .
```

> **What is an image?**  
An image is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and configuration files.

**Step 2: Run the container**
```bash
docker run -it test:pandas 2024-06-20
```

`2024-06-20` is an argument.   
Since the entry point of the image is `["python", "pipeline.py"]`, running the container will execute the python script.

> **What is a container?**  
A container is a lightweight, portable, and self-sufficient unit that encapsulates an application and its environment, enabling it to run consistently across different computing environments.
> - Encapsulation
> - Isolation
> - Portability

![run docker](2_docker_sql/img/run-docker.png)

## Run Postgre in Docker
