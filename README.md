# Login page made in Python

## Overview
This app is a login website built on Flask as a Backend, HTML and CSS as a Frontend and MySQL as Database. You can create users, delete users or reset passwords of the users but first you need to log in with an existing user stogered in the Database. 

## Infrastructure
### Local
You can run this app in your machine with the command `python main.py` but you will need to have python installed and provide the MySQL Database. Also, you will need to create a **.env** file with the following env variables:
- **PORT**
- **DB_HOST**
- **DB_USER**
- **DB_PASSWORD**
- **DB_SCHEMA**\

### Docker
This app can be deployed in Docker using the `docker-compose.yml` file. Before running the docker-compose, you will need to create a Docker volume for the MySQL container:
- `docker volume create db-mysql`

### Kubernetes
This repository includes the deployment YAML files to run the application in a Kubernetes Cluster.
