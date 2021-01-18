# Instagram

Author:[Stephen Nderitu](https://github.com/Steve99-coder)  
  
# Description  

This is a clone of the website for the Instagram app where users share their  images and ideas for other users to view them.Users can Sign in to the application,Upload pictures to the application,See their profile with all their pictures.[View Site](https://evening-wildwood-32640.herokuapp.com/)


## User Story  
  
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  

  
## Setup and Installation  
 
### Clone the repository:  
 ```bash 
 https://github.com/Steve99-coder/instagram.git
```
### Navigate into the folder 
 ```bash 
cd into insta master
```
### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
### Setup your Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```

### Running the application  
 ```bash 
 python manage.py runserver 
```
### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Django 3.1.5](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Python3.8.5](https://www.python.org/)  
* [Bootstrap4](https://getbootstrap.com/)


## Contact Information   
Please email me at stevenderitu99@gmail.com for any question or contributions,
  
## License 

MIT <br>
Copyright © by Stephen Nderitu 2021