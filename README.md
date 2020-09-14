# health-insurance-project


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)


<!-- ABOUT THE PROJECT -->
## About The Project


The project aims at creating a simple Store/Retrieve application in the health insurance industry.
The project currently works to mimic the daily transactions happening in the given scenario.

The backend database used for the project was created using freemysqlhosting.net.


### Built With
The project is built using Flask and supported by MySQL and JavaScript.
* [Flask] --> Framework
* [MySQL]--> Backend Services
* [JavaScript]--> Front End UI, Validations

<!-- GETTING STARTED -->
## Getting Started

The instructions and prerequisites are given with the intention that it should work for a brand new computer.
All the installation steps need not be followed. Adviceable to install packages in virtual environment.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.x or (Latest Version)
* pipenv
* Flask 1.1.2 or (Latest Version)
* pip 20.2.3 or (Latest Version)

### Installation


1. Clone the repo
```sh
git clone https://github.com/naveendayakar/health-insurance-project.git
```
2.Install all below in terminal
```sh
install Brew
brew install pipenv
brew install mysql
brew install mysql-client
```

3. In the downloaded directory (pipenv used for virutal environment)
```sh
pipenv install flask
from flask import flask
pipenv install flask-mysqldb
pipenv shell
```
4. Run the App:
```JS
python app.py
```
5. Go to the localhost address displayed in the terminal, via the browser
 http://127.0.0.1:5000/
