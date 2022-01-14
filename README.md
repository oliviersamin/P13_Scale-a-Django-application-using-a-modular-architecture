# P13_Scale-a-Django-application-using-a-modular-architecture
***
## Table of contents
1. [Program surroundings](#program-surroundings)
2. [The five principal aims of this project](#the-five-principal-aims-of-this-project)
3. [Used configuration](#used-configuration)
4. [Get and launch the app in local](#get-local-app)
5. [Use the CircleCI pipeline](#CircleCI_CD)
***

## Program surroundings <a name="program-surroundings"></a>

This program is the last of thirteen projects to be validated in order to get a degree as a developer in Python applications.  

For more info on that subject please visit the following website:  
https://openclassrooms.com/fr/paths/322-developpeur-dapplication-python
  

## The five principal aims of this project <a name="the-five-principal-aims-of-this-project"></a>
* Refactor an app to minimize the technical debt
* Apply a modularity architecture in a Python app
* Use CircleCI to manage the production of code with the CI/CD methodology
* Deploy the app with Heroku
* Use Sentry to set up a system of code control

## Used configuration <a name="used-configuration"></a>
OS: Linux Mint 20.2 Cinnamon 5.0.7
Python: 3.8.10 (default, Nov 26 2021, 20:14:08)
Django: 3.2.6

## Get and launch the app in local <a name="get-local-app"></a>
* Clone the repository  
  * `cd /path/to/put/project/in`  
  * `git clone https://github.com/oliviersamin/P13_Scale-a-Django-application-using-a-modular-architecture.git`

* Create the virtual environment
  * `cd /path/to/Python-OC-Lettings-FR`
  * python3 -m venv env
  * activate the virtual environment: `source env/bin/activate`

* Launch the app
    * `cd /path/to/Python-OC-Lettings-FR`
    * `source venv/bin/activate`
    * `pip install -r requirements.txt`
    * `python manage.py runserver`
    * Go on http://localhost:8000 in a web browser.

## Deployment <a name="CircleCI_CD"></a>
CircleCI has been used to deploy the app on Heroku
#### Principles of deployment
Each time you push a modification on the GitHub repo, the CircleCI pipeline will start.  
This pipeline allows you to provide continuous integration and delivery for this project.  
The pipeline includes the usual steps for continuous integration:
1. compile the code
2. test the code
3. build the image using the new code
4. push the image to Dockerhub
5. push the image to Heroku
6. deploy the Heroku app

#### Configuration
The required configuration is as follow:
* Fork the GitHub repo on your computer to be able to push new features
* 

#### Usage
TO DO
