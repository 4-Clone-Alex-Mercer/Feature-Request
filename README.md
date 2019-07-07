# Feature-Request-App

An application for IWS clients to request features, it gives employees the ability to view, create, edit, and delete client requests, every request has priority related to a specific client, that helps the employee to determine when to implemet the feature for that client, and all the priorities for the client's requests will get reordered accordingly whenever we create a new request or edit an existing one.

### Check out the App at the following link. 
[Live Demo](http://172.105.66.84/)


## Stack
1. Python Flask: Flask is a micro framework for python
2. SQLAlchemy: ORM for SQL DBs
3. MYSQL: Relational DB used
4. JQuery: JavaScript Library
5. Kendo: JQuery UI components library

![alt text](https://imgur.com/wDO9uqi.png)

## Folders architecture

![alt text](https://imgur.com/ItZsVSS.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

You will need to install the following to be able to run the application.
```
Python 3.7 
Pip
Git
```



### Installing

A step by step series of examples that tell you how to get a development env running locally:

1. First clone the repo

```
git clone https://github.com/Besslan/Feature-Request.git
``` 

2. Set the environment keys, the database connection and the secret key in the config.py file


SECRET KEY: The secret key is required to keep the client-side sessions secure, it could be any string but it is recommended to be random and complix . 


SQLALCHEMY_DB_URI: SQLAlchemy supports many sql databasses and each have thier own uri, an example of a mysql uri would be:

mysql://yourusername:yourpassword@yourserver/yourDB


```
sudo nano ~/.profile

export SECRET_KEY='YOUR_SECRET_KEY' 
export SQLALCHEMY_DB_URI='YOUR_DATABASE_URI'
```
Depending on the selected database and uri create the database and example for mysql would be the following:

```
mysql -u yourusername -p
```
Enter the password when asked for and continue. Then run the following to create the database.
```
CREATE DATABASE yourDB;
```
3. Installing the dependinces

Open the terminal in the project folder:

Install pipenv virtual environment.
```
pip install pipenv
```
Activate the virtual environment and install the required dependencies by running the following commands, make sure the environment is activated for the following commands.
```
pipenv shell
pipenv install
```

4. Create database tables and insert initial data:

```
python run.py
``` 
Now you have a running instance of this application on http://localhost:5000/


## Running the tests
First make sure to go through [installation](#installing) steps from 1 to 3, then run the following:

```
python run.py
``` 
And to run the test coverage:

```
coverage run -m pytest tests.py
``` 
To open the coverage report run:
```
coverage report
``` 
## Deployment
The application is deployed on an ubuntu server on linode using nginx & gunicorn.

