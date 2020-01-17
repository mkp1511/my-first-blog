(1)
$ mkdir djangogirls
(2)
$ cd djangogirls
(3)
$ python3 -m venv girls
(4)
$ source girls/bin/activate
(girls)$

# Now on (i.e. after the activation of virtual environment) you can use python in place of python3 
# because the environment has the python3 version only

(5)
# A requirements file keeps a list of dependencies to be installed using pip install:
Create a requirements.txt file inside of the djangogirls/ folder, using your editor.

# Your directory will look like this:

# djangogirls
# ├── girls
# │   └── ...
# └───requirements.txt

(6)
In your djangogirls/requirements.txt file you should add the following text:

djangogirls/requirements.txt
Django~=2.2.4

(7)
# Now, run pip install -r requirements.txt to install Django.

(girls) ~/djangogirls$ pip install -r requirements.txt
    Collecting Django~=2.2.4 (from -r requirements.txt (line 1))
    Downloading Django-2.2.4-py3-none-any.whl (7.1MB)
    Installing collected packages: Django
    Successfully installed Django-2.2.4

(8)
# create a new django project
(girls) ~/djangogirls$ django-admin startproject mysite .

# django-admin.py is a script that will create the directories and files for you. You should now have a directory structure 
# which looks like this:

# djangogirls
# ├── manage.py
# ├── mysite
# │   ├── __init__.py
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py
# ├── myvenv
# │   └── ...
# └── requirements.txt

(9) 
Edit the setting.py file, No need to change the database setting as we are using the default database sqlite3.
ensure that it has the following entries:
(i) LANGUAGE_CODE = 'en-us'
(ii) TIME_ZONE = 'Asia/Kolkata'
(iii) STATIC_URL = '/static/'
(iv) STATIC_ROOT = os.path.join(BASE_DIR, 'static')
(v) ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

(10) creating an application
(girls) ~/djangogirls$ python manage.py startapp blog

# You will notice that a new blog directory is created and it contains a number of files now. 
# The directories and files in our project should look like this:

# djangogirls
# ├── blog
# │   ├── admin.py
# │   ├── apps.py
# │   ├── __init__.py
# │   ├── migrations
# │   │   └── __init__.py
# │   ├── models.py
# │   ├── tests.py
# │   └── views.py
# ├── db.sqlite3
# ├── manage.py
# ├── mysite
# │   ├── __init__.py
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py
# ├── myvenv
# │   └── ...
# └── requirements.txt

(11)
After creating an application, we also need to tell Django that it should use it. 
We do that in the file mysite/settings.py -- 
open it in your code editor. We need to find INSTALLED_APPS and add a line containing 'blog.apps.BlogConfig', just above ]. 
So the final product should look like this:

mysite/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
]

(12)
Creating a blog post model
In the blog/models.py file we define all objects called Models – this is a place in which we will define our blog post.

Let's open blog/models.py in the code editor, remove everything from it, and write code like this:

blog/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

(13)
Create tables for models in your database
# The last step here is to add our new model to our database. 
# First we have to make Django know that we have some changes in our model. 
# (We have just created it!) 
# Go to your console window and type python manage.py makemigrations blog. It will look like this:

(girls) ~/djangogirls$ python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py:
  - Create model Post
Note: Remember to save the files you edit. 
Otherwise, your computer will execute the previous version which might give you unexpected error messages.

(14)
# Django prepared a migration file for us that we now have to apply to our database. 
Type python manage.py migrate blog and the output should be as follows:


(girls) ~/djangogirls$ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK

(15) Django admin
# To add, edit and delete the posts we've just modeled, we will use Django admin.

Let's open the blog/admin.py file in the code editor and replace its contents with this:

blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)

# As you can see, we import (include) the Post model defined in the previous chapter. 
# To make our model visible on the admin page, we need to register the model with admin.site.register(Post).

(16) Create superuser
(girls) ~/djangogirls$ python manage.py create superuser

# superuser details
# username: ola
# email: ola@example.com
# password: olamkrain

