# Eureka !



## Tags

[Python](https://www.python.org), [Docker](https://docker.com), [docker-compose](https://docs.docker.com/compose/), [django](https://www.djangoproject.com/), [django rest framework](https://www.django-rest-framework.org/), [mySQL](https://www.mysql.com/). 

---

## Table of contents 

[Project Phases](#project-phases) <br>
[Description](#description) <br>
[Before We Get Started](#before-we-get-started) <br>
[Architechture](#architechture) <br>
[Data Structure](#data-structure) <br>
[What is Docker ?](#what-is-docker?) <br>
[Get started](#get-started) <br>
[Routes](#routes) <br>
[Security](#security) <br>
[Tests](#tests) <br>
[What's Next ?](#what's-next?) <br>

---

## Project Phases

- [x] pre-development
- [x] development
- [x] tests
- [x] release v 1.0

---

## Description

This project was developed due academic reasons and developed all by myself. Let me explain what it is:

This is a CRUD (Create, Read, Update, Delete) REST (Representational State Transfer) API (Application Programing Interface) that will run in Docker developed in python 3.10. That will be able to perform CRUD actions into a Students database. 

This is a microservice application and I decided to develop a dockerized app due its possibility on run in any device with the same performance, avoiding versioning problems. And besides that, docker is cool !

The database chosen for this project was MySQL and this application already have some data stored to make this project looks more realistic. 

---

## Before We Get Started

As I mentioned before this application is dockerized, with that in mind you will need to setup docker in your machine, if it is not installed. 

---

## Architechture

This is the architecture tree of this project:

eureka<br>
├───.dbdata<br>
│   ├───eureka<br>
│   ├───mysql<br>
│   ├───performance_schema<br>
│   └───sys<br>
├───eureka<br>
│   └───__pycache__<br>
└───students<br>
    ├───migrations<br>
    │   └───__pycache__<br>
    └───__pycache__<br>
<br>

---

## Data Structure

This is how the main table was set: 

students: 

| NN | PK | ID         | integer   | autoincrement |    <br/>
| NN |    | first_name | varchar   | max 200       |    <br/>
| NN |    | last_name  | varchar   | max 200       |    <br/>
| NN | UQ | email      | varchar   | max 200       |    <br/>
| NN |    | age        | integer   |               |    <br/>
| NN |    | grade      | varchar   | max 30        |    <br/>
| NN |    | period     | varchar   | max 40        |    <br/>
|    |    | created_at | timestamp |               |    <br/>
|    |    | updated_at | timestamp |               |    <br/>

NN not null <br>
PK primary key <br>
UQ unique <br>


---

## What is Docker ?

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.


- [Docker](https://docker.com)


---

## Get Started

1. Dowload and install [Docker](https://docker.com).
2. Check if docker-compose was installed successfuly.
3. Clone this repository.
4. Open the repository folder.
5. Run: _"docker-compose run"_
6. Hit these endpoints in [Routes](#routes) section.
7. if there is any doubt in how to run this API, please go to [Tests](#tests) section.
8. Any doubts or suggestions, please feel free to hit me up anytime @dribeiroferr (:


---

## Routes

Base URL: <br>
```
http://localhost:8000

``` 
List all students:

```
[GET] http://localhost:8000/api/students

``` 
Create students:

```
[POST] http://localhost:8000/api/students

''' 
the information needed is like that: 

{
	"first_name": "Tony",
	"last_name": "Stark",
	"email": "tony@starkindustries.com",
	"age": "17",
	"grade": "eletronics",
	"period": "morning"
}


'''
``` 

Retrieve students by id:

```
[GET] http://localhost:8000/api/students/{id}

[example] http://localhost:8000/api/students/1

``` 

Update students by id:

```
[PUT] http://localhost:8000/api/students/{id}

[example] http://localhost:8000/api/students/1

``` 

Remove students by id:

```
[DELETE] http://localhost:8000/api/students/{id}

[example] http://localhost:8000/api/students/1

``` 

---

## Security

 If it was a "real world application" all these exposed data would be protected by layers of middlewares, SSL (Secure Socket Layer) protocols, and all its environment variables and .config archives would be added to _.gitignore_ file, or excluded from it, while pushing to a new repository. 


---

## Tests

Tests were performed on Kali linux (debian based) Operational System with success ! 

### Steps to reproduce: 

1. Update apt (Advanced Package Tool):
   
    ```
    $ sudo apt update
    ```

2. After the apt has been updated run the command below to install docker:
   
    ```
    $ sudo apt install -y docker.io 
    ```

3. Check if docker was installed successfuly by: 
   
    ```
    $ sudo docker --version
    ```

4. The output has to be something like that: 
    
    ```
    Docker version 20.xx.x, build xxxxxxx
    ```

5. Install docker-compose by:

    ```
    sudo apt install -y docker-compose
    ```

6. Check if docker-compose was installed successfuly by: 

    ```
    $ sudo docker-compose --version
    ```
7. The output has to be something like that: 
   
    ```
    docker-compose version 1.xx.x, build xxxxxxx
    ```

8. Now we are able to run this application. Run:
   
    ```
    git clone https://github.com/dribeiroferr/eureka.git

    cd eureka

    docker-compose up
    ```
9. The container will be built and after that you should reach that endpoint by copy and paste to your web browser: 

    ```
    http://localhost:8000/api/students

    ```


---

## What's next ?

I am thinking about to develop a frontend system to connect with this API so users will be able to use a pretty GUI and perform all CRUD operations they want to. 

---

- @dribeiroferr

