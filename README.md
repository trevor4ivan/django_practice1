Personal_website with Django steps
Create the root directory.
Create the project root directory as a folder on the desktop, name is django_practice1, right click and open with vscode or open the root directory with the following command inside terminal: mkdir django_practice
Create the virtual environment.
Cd into django_practice1 directory and create the virtual environment.
Create a virtual environment using the venv module with the command python -m venv .venv or pip install virtualenv
The name of the virtual environment directory is .venv and the period that precedes the virtual environment directory indicates that the directory will be hidden.
Activate the virtual environment
Inside the django_practice1 directory use the following command to activate the virtual environment: .venv/scripts/activate
Or using the gitbash terminal use the following command: source .venv/scripts/activate
Install Django
With the virtual environment activated and at the root of django_practice1 directory, use the following command to install Django package: pip install django
Start a new project
With the virtual environment activated and at the root of django_practice1 directory, use the following command to start a new project and name the new project django_project: django-admin startproject personal_website_project .
The period after the personal_website_project name is intentional; this will make Django to place all the files inside one single directory.
Apply migrations
When Django created the personal_website_project directory, several built-in apps were created along .
We need to apply migrations so that these changes can be applied to the database.
With the virtual environment activated, and at the root of django_practice1 directory, use the following command to apply migration: python manage.py migrate
Start the development server
With the virtual environment activated and at the root of django_practice1 directory, use the following command to start the development server: python manage.py runserver
Stop the development server with the following command: ctrl + c
Starting an app.
With the virtual environment activated and at the root of django_practice1, use the following command to start an app named pages: python manage.py startapp pages1.
Add the pages1 app to the list of installed apps inside the personal_website_project directory settings
Create a view
Open the view.py file of pages app and write the following codes
from django.http import HttpResponse
from django.shortcuts import render
def home_page_view(request):
	return HttpResponse(“Homepage”)
def about_page_view(request):
	context = {
“name”: “Alice”,
“Age”: 40, 
}
	return render(request, “pages1/about.html”, context)

Create the about.html template inside view.py file of pages1 app
By default, Django’s template loading engine looks for a “templates” subdirectory in each app.
At the root of Django_practice1 with the virtual environment activated, right click pages1 app and create a directory named templates, right click the templates directory and create another subdirectory named pages1, right click the pages1 subdirectory and create a file named about.html
Update the about.html file
Open the about.html file inside the pages1 app and add the following codes;
<h1>About page</h1>
<p>My name is {{ name }}. I am {{ age }} years old.</p>
Create a urls.py file inside the pages1 app
we need to match a url path to this view function.
create a urls.py file inside the pages app and write the following code
from django.urls import path
from .views import home_page_view, about_page_view 
urlpatterns = [
path( “”, home_page_view),
path(“about/”, about_page_view)
]
update the urls.py (gateway to other urls) file inside the root directory of personal_website_project
There is an built-in urls.py file inside the root directory personal_website_project
Open the urls.py file and import the following code:
From django.urls import path, include
Add the pages1 app url path to the list of the url inside the urls.py file of  personal_website_project directory
The urls.py file has an inbuilt admin url path
urlpatterns = [
path(“admin/”, admin.site.urls),
path(“”, include(“pages1.urls”),
path(“about/”, include(“pages1.urls”),
]
Start the development server with python manage.py runserver.
This will display hello world
.GITIGNORE FILE
At the root of django_practice1, create a file and name it .gitignore.
This will be used to store the virtual environment, to prevent it from been pushed to github.
Open the .gitignore file and add .venv
__pycache__/
db.sqlite3
testing
Since no database is involved in our project, we will import SimpleTestCase at the top of the file. For our first tests, we’ll check that the two URLs for our website, the Homepage and About page, return HTTP 200 status codes, the standard response for a successful HTTP request.
With virtual environment activated and at the root of django_practice1
Open the test.py file of the pages1 app and add the following codes.
from django.test import SimpleTestCase
class HomepageTests(SimpleTestCase):
def test_url_exists_at_correct_location(self):
response = self.client.get("/")
self.assertEqual(response.status_code, 200)

class AboutpageTests(SimpleTestCase):
def test_url_exists_at_correct_location(self):
response = self.client.get("/about/")
self.assertEqual(response.status_code, 200)

Stop the development server with ctrl + c
Use the following command to test python manage.py test

Storing the installed packages of the virtual environment
Record of installed packages inside virtual environment
With virtual environment activated at the root of django_practice1, use the following command to store the packages inside a requiremens.txt file.
pip freeze> requirement.txt
pushing to github account
stop the development server with ctrl + c and at the root of django_practice1 directory, deactivate the virtual environment with the following command: deactivate
go to github account and create a repository named django_pracitce1
At the root of django_practice1 directory, use the following command to initialize git and push the code to github
git init
git add -A
git commit -m “first commit”
git branch -M main
git remote add origin https://github.com/trevor4ivan/django_practice1.git
git push -u origin main

