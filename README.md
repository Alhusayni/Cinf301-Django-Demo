# Cinf301-Django-Demo

Abdulrahman Alhusayni

## Getting Started:


You should download Python 3 and add it to the PATH.

you can use Pycharm for coding which is very great IDE.

After installing Python3, Go to the CMD and write this command: 
```
pip install django
```



### Creating a project:


To start a project use the commandline and go to your working directory and write this command: 
```
django-admin startproject <projectname> 
```

Then django will do the rest and create the initial files.

Then run this command: 
```
python manage.py runserver
```

Now you will see your work is running

### Accessing admin page:


First you should create tables by using this command :
```
python manage.py migrate
```

then create superuser to access admin page run this command:
```
python manage.py createsuperuser 
```

### Creating starting app:


To create a starting app, you should write this command in your working directory:
```
python manage.py startapp <appname>
```

then go to setting.py and type your app's name in INSTALLERD_APP = [

#### Note :



When you add models you should run this command:
```
python manage.py makemigrations
```

