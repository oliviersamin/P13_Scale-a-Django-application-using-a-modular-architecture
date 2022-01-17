# P13_Scale-a-Django-application-using-a-modular-architecture
***
## Table of contents
1. [Program surroundings](#program-surroundings)
2. [The five principal aims of this project](#the-five-principal-aims-of-this-project)
3. [Used configuration](#used-configuration)
4. [Get and launch the app in local](#Get-and-launch-the-app-in-local)
5. [Deployment](#deployment)
***

<a name="program-surroundings"></a>
## Program surroundings 


This program is the last of thirteen projects to be validated in order to get a degree as a developer in Python applications.  

For more info on that subject please visit the following website:  
https://openclassrooms.com/fr/paths/322-developpeur-dapplication-python
  

<a name="the-five-principal-aims-of-this-project"></a>
## The five principal aims of this project 
* Refactor an app to minimize the technical debt
* Apply a modularity architecture in a Python app
* Use CircleCI to manage the production of code with the CI/CD methodology
* Deploy the app with Heroku
* Use Sentry to set up a system of code control

<a name="used-configuration"></a>
## Used configuration 
OS: Linux Mint 20.2 Cinnamon 5.0.7
Python: 3.8.10 (default, Nov 26 2021, 20:14:08)
Django: 3.2.6


<a name="Get-and-launch-the-app-in-local"></a>
## Get and launch the app in local 
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


<a name="deployment"></a>
## Deployment
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
7. monitor the possible errors with Sentry


#### Configuration
The required configuration is as follows:
* Access to the GitHub repo
* Access to the DockerHub site and related repo
* DockerHub link to the repo: https://hub.docker.com/r/olivierfuerte/p13_ci_cd
* Access to CircleCI site and repo related to the CI/CD pipeline  
  * All the sensible data are stored in the "Organization settings" under the context named "Basic secured data"
  * The secured data contain the DockerHub repo name, the Docker credentials and the Heroku app name 
* Access to the Heroku site and the related repo
* Heroku's link to the app: https://git.heroku.com/oc-lettings-os.git
* Access to the Sentry Site and the related repo

#### Usage
1. Fork the GitHub repo on your computer to be able to push new features


2. Once a modification has been made in the repo on GitHub (after a push or directly from GitHub) the CI/CD pipeline will be launched automatically  
a. if the modification has been made on the main branch then the pipeline will run all the steps from 1 to 6 described in the  Principles of deployment section above  
   b. if the modification has been made on another branch then the pipeline will run only the steps 1 and 2 described in the  Principles of deployment section above

   
3. To access and modify this CI/CD pipeline go to the CircleCI site:  
   a. click on the corresponding project name  
   b. select the main branch  
   c. click on the "edit config" button to display the config file  
   d. each time a modification is made in the config file the pipeline is launched according to the explanations given in the  2. of this usage section  
   e. REMINDER: if environment variables are modified, remember to modify the value in the context named "Basic secured data" 


4. Once the pipeline is done, a new deployment is available on the Heroku application.  
To launch the app, click on the "open app" button, and it is online.  

   
5. Once the app is online, the monitoring is done by Sentry.  
   Go on their website on the corresponding repo and click on the "issues" button. 
   