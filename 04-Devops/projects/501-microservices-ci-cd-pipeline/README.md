# Project 501: Microservices CI/CD Pipeline

## Description

This project aims to create full CI/CD Pipeline for microservice based applications using [Spring Petclinic Microservices Application](https://github.com/spring-petclinic/spring-petclinic-microservices). Jenkins Server deployed on Elastic Compute Cloud (EC2) Instance is used as CI/CD Server to build pipelines.

## Introduction

Click to see project planning cycles of [the Petclinic Application](./microservice-project-501-planning.pdf).

## Flow of Tasks for Project Realization

| Epic | Task  | Students Task | Teachers Task | Task Definition   | Branch  |
| ---   | :---  | ---           | ---           | :---              | :---    |
| Preparation | Prepare Public Repo for Students | | Task-1 | Prepare Microservices Project Public Repository for Students on GitHub |
| Preparation | Prepare Public Repo for Teachers | | Task-2 | Prepare Microservices Project Private Repository for Teachers on GitHub |
| Introduction | Introduction to the Petclinic Application | | Task-3 | Prepare Slides for Introduction of Petclinic App |
| Introduction | Showcase the Petclinic Application on Demo Server | | Task-4 | Prepare Demo Server for Petclinic App on AWS EC2 |
| Local Development Environment | Prepare Development Server Manually on EC2 Instance| MSP-1 | | Prepare development server manually on Amazon Linux 2 for developers, enabled with `Docker` , `Docker-Compose` , `Java 11` , `Git` .  |
| Local Development Environment | Prepare GitHub Repository for the Project | MSP-2-1 | | Fork and clone the Petclinic app from the Clarusway repository [Petclinic Microservices Application](https://github.com/clarusway/petclinic-microservices.git) |
| Local Development Environment | Prepare GitHub Repository for the Project | MSP-2-2 | | Prepare base branches namely `master` , `dev` , `release` for DevOps cycle. |
| Local Development Environment | Check the Maven Build Setup on Dev Branch | MSP-3 | | Check the Maven builds for `test` , `package` , and `install` phases on `dev` branch |
| Local Development Environment | Prepare a Script for Packaging the Application | MSP-4 | | Prepare a script to package the application with Maven wrapper | feature/msp-4 |
| Local Development Environment | Prepare Development Server Cloudformation Template | MSP-5 | | Prepare development server script with Cloudformation template for developers, enabled with `Docker` , `Docker-Compose` , `Java 11` , `Git` . | feature/msp-5 |
| Local Development Build | Prepare Dockerfiles for Microservices | MSP-6 | | Prepare Dockerfiles for each microservices. | feature/msp-6 |
| Local Development Environment | Prepare Script for Building Docker Images | MSP-7 | | Prepare a script to package and build the docker images for all microservices. | feature/msp-7 |
| Local Development Build | Create Docker Compose File for Local Development | MSP-8-1 | | Prepare docker compose file to deploy the application locally. | feature/msp-8 |
| Local Development Build | Create Docker Compose File for Local Development | MSP-8-2 | | Prepare a script to test the deployment of the app locally. | feature/msp-8 |
| Testing Environment Setup | Implement Unit Tests | MSP-9-1 | | Implement 3 Unit Tests locally. | feature/msp-9 |
| Testing Environment Setup | Setup Code Coverage Tool | MSP-9-2 | | Update POM file for Code Coverage Report. | feature/msp-9 |
| Testing Environment Setup | Implement Code Coverage | MSP-9-3 | | Generate Code Coverage Report manually. | feature/msp-9 |
| Testing Environment Setup | Prepare Selenium Tests | MSP-10-1 | | Prepare 3 Selenium Jobs for QA Automation Tests. | feature/msp-10 |
| Testing Environment Setup | Implement Selenium Tests | MSP-10-2 | | Run 3 Selenium Tests against local environment. | feature/msp-10 |
| CI Server Setup | Prepare Jenkins Server | MSP-11 | | Prepare Jenkins Server for CI/CD Pipeline. | feature/msp-11 |
| CI Server Setup | Configure Jenkins Server for Project | MSP-12 | | Configure Jenkins Server for Project Setup. | |
| CI Server Setup | Prepare CI Pipeline | MSP-13 | | Prepare CI pipeline (UT only) for all `dev` , `feature` and `bugfix` branches. | feature/msp-13 |
| Registry Setup for Development | Create Docker Registry for Dev Manually | MSP-14 | | Create Docker Registry on AWS ECR manually using Jenkins job. | |
| Registry Setup for Development | Prepare Script for Docker Registry| MSP-15 | | Prepare a script to create Docker Registry on AWS ECR using Jenkins job. | feature/msp-15 |
| QA Automation Setup for Development | Create a QA Automation Environment | MSP-16 | | Create a QA Automation Environment with Docker Swarm. | feature/msp-16 |
| QA Automation Setup for Development | Prepare a QA Automation Pipeline | MSP-17 | | Prepare a QA Automation Pipeline on `dev` branch for Nightly Builds. | feature/msp-17 |
| QA Setup for Release | Create a Key Pair for QA Environment | MSP-18-1 | | Create a permanent Key Pair for Ansible to be used in QA Environment on Release. | feature/msp-18 |
| QA Setup for Release | Create a QA Infrastructure with AWS Cloudformation | MSP-18-2 | | Create a Permanent QA Infrastructure for Docker Swarm with AWS Cloudformation. | feature/msp-18 |
| QA Setup for Release | Create a QA Environment with Docker Swarm | MSP-18-3 | | Create a QA Environment for Release with Docker Swarm. | feature/msp-18 |
| QA Setup for Release | Prepare Build Scripts for QA Environment | MSP-19 | | Prepare Build Scripts for creating ECR Repo for QA, building QA Docker images, deploying app with Docker Compose. | feature/msp-19 |
| QA Setup for Release | Build and Deploy App on QA Environment Manually | MSP-20 | | Build and Deploy App for QA Environment Manually using Jenkins Jobs. | feature/msp-20 | 
| QA Setup for Release | Prepare a QA Pipeline | MSP-21 | | Prepare a QA Pipeline using Jenkins on `release` branch for Weekly Builds. | feature/msp-21 |
| Staging and Production Setup | Prepare Petlinic Kubernetes YAML Files | MSP-22 | | Prepare Petlinic Kubernetes YAML Files for Staging and Production Pipelines. | feature/msp-22 |
| Staging and Production Setup | Prepare HA RKE Kubernetes Cluster | MSP-23 | | Prepare High-availability RKE Kubernetes Cluster on AWS EC2 | feature/msp-23 |
| Staging and Production Setup | Install Rancher App on RKE K8s Cluster | MSP-24 | | Install Rancher App on RKE Kubernetes Cluster| |
| Staging and Production Setup | Create Staging and Production Environment with Rancher | MSP-25 | | Create Staging and Production Environment with Rancher by creating new cluster for Petclinic | |
| Staging Deployment Setup | Prepare a Staging Pipeline | MSP-26 | | Prepare a Staging Pipeline on Jenkins Server | feature/msp-26|
| Production Deployment Setup | Prepare a Production Pipeline | MSP-27 | | Prepare a Production Pipeline on Jenkins Server | feature/msp-27|
| Production Deployment Setup | Set Domain Name and TLS for Production | MSP-28 | | Set Domain Name and TLS for Production Pipeline with Route 53 | feature/msp-28|
| Production Deployment Setup | Set Monitoring Tools | MSP-29 | | Set Monitoring tools, Prometheus and Grafana | |

## MSP 1 - Prepare Development Server Manually on EC2 Instance

- Prepare development server manually on Amazon Linux 2 for developers, enabled with `Docker`, `Docker-Compose`, `Java 11`, `Git`.

```bash
# update os
sudo yum update -y
# set hostname as petclinic-dev-server
sudo hostnamectl set-hostname petclinic-dev-server
# install docker
sudo amazon-linux-extras install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user
# install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
# install JDK 11
sudo yum install java-11-amazon-corretto -y
# install Git
sudo yum install git -y
```

## MSP 2 - Prepare GitHub Repository for the Project

- Fork the Petclinic app from the Clarusway repository [Petclinic Microservices Application](https://github.com/clarusway/petclinic-microservices.git)

- Rename the forked repo on your GitHub as `microservices-ci-cd-pipeline-with-petclinic-app`.

- Clone the forked repo from your GitHub repo on development server.

```bash
git clone https://github.com/callahan-cw/microservices-ci-cd-pipeline-with-petclinic-app.git
```

- Prepare base branches namely `master`, `dev`, `release` for DevOps cycle.

  - Create `dev` base branch.

    ```bash
    git branch # show local branches
    git branch -a # shows all branches local and remote
    git checkout master
    git branch dev
    git checkout dev
    git push --set-upstream origin dev
    ```

  - Create `release` base branch.

    ```bash
    git fetch # will get latest info from the remote repo
    git checkout master
    git branch release
    git checkout release
    git push --set-upstream origin release
    ```

## MSP 3 - Check the Maven Build Setup on Dev Branch

