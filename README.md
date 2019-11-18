# Instaclone

###  Author
nignanthomas

### Description
Instaclone is a clone of the website for the popular photo app Instagram(desktop version)

### User Stories
1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

### How to use
To use Instaclone, you must login/register. Once logged in, you will be able to see posts made by other users.
You can add your own photos from your profile page.
As a user you can also follow other users and view images posted by those users.
You also have the possibility to edit your profile and view the photos that you have posted.


### Tech used
1. HTML and CSS
2. Python
3. Django
1. Postgres
1. Heroku for deployment

## Set up and Installation
### Prerequisites
You will need to install git, django, postgres and python3.6+ installed in your machine.
To install these packages, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==1.11

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

### Installation
1. To access this application on your command line, you need to clone it
`git clone https://github.com/nignanthomas/Instagram.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3.6 manage.py runserver`
1. You can make changes to the db with
`python3.6 manage.py makemigrations instaclone`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test instaclone`



### Known Bugs
No known bugs.

### Live link
https://github.com/nignanthomas/Instagram

### Licence
This project is under the [MIT](https://github.com) licence

Copyright (c) 2018 nignanthomas
# INSTACLONE-
