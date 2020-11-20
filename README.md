## Simple django instructions

`$ pip3 install django`
pip3 installs to python3
pip installs to python2

Site packages (installed libs) live Here
- `/workspace/.pip-modules/lib/python3.8/site-packages`

`$ cd -` - go to prev dir

Start a project in Django
- `$ django-admin startproject django_todo .` the . says make project in current directory

Running the app
- `python3 manage.py runserver`

# Simple Route
Create an app (a module that can be used by the main app)
- `python3 manage.py startapp todo`
- Create the todo app
- In the new todo folder the app created open views.py
- import `HttpResponse` from django.shortcuts
- `def say_hello(request):`
    - `return HttpResponse("Hello!")`
- Creates a view
- Give a route to this view in django_todo > urs.py
    - from here import the route `from todo.views import say_hello`
- define the url for this view with path function
    - path('hello/', say_hello, name='hello')
    - is URL, view function, name

## Regarding Templates

The folder structure of todo/templates/todo/todo_list.html makes sure
django finds the correct template for this particular app.  If another app
has the same name it could be problomatically returned first

- views.py
    - `return render(request, 'todo/todo_list.html')`
- urls.py
    - `path('', get_todo_list, name='get_todo_list')`
- settings.py
    - add `todo` to `INSTALLED_APPS = []`


## Databases and migration
Django allows you to write pythn code to interact with databases and it will handle the database language its self
It uses migrations to handle database operations

`$ python3 manage.py makemigrations --dry-run` - See what changes have been made without migrating

`$ python3 manage.py makemigrations` - Create migration files

`$ python3 manage.py showmigrations` - Show migrations that need applying

`$ python3 manage.py migrate --plan` - show what is and isnt applied

`$ python3 manage.py migrate` - apply all migrations

### login to database as admin

- Create superuser python3 manage.py createsuperuser
- fill in details / kelvinhere / superuserpassword

* login through the /admin path from running app

## Example of getting values to a database

- look in todo/models.py
- Once fields have been created you need to migrate do a dryrun first to see what changes will be made
- `$ python3 manage.py makemigrations --dry-run`
- This will show you the directories where migration files will be created
- If happy run `python3 manage.py makemigrations`
- Apply and migreate these changes with `python3 manage.py migrate`

* Register these files in todo/admin.py and add for example
* `from .models import Item`
* `admin.site.register(Item)`
* This import Item from models.py in this directory and registers them, they will be visible on admin page now.

- You can now to to /admin find the Item collection and add items

### Rendering values to page

- Start is todo/views.py
- `from .models import Item` will allow us to use the Item model in our views
- `items = Item.objects.all()`
- `context = {'items': items}`
- `return render(request, 'todo/todo_list.html', context)` will allow our page to access the context variable created from our Items model

### Submitting a from

- Same way as flask but include just after <form>
- {% csrf_token %}
- This creates a unique token to make sure POST is coming from correct form and not forged


## Django testing

the test.py file has already imported TestCase from django.test this is an extension of pythons own unittest.

run the tests with `python3 manage.py test`

as long as a file starts with test it will be picked up when running tests example you could have 3 test files in the todo folder
- test.py
- test_views.py
- test_logic.py

to only pick a specific test file to run 
- `python3 manage.py test todo.test_forms`

to only run a class of tests in a specific file
- `python3 manage.py test todo.test_forms.TestItemForm`

to only run a specific test ina specific class in a specific file
- `python3 manage.py test todo.test_forms.TestItemForm.test_fields_are_explicit_in_form_metaclass`

### Coverage - test %
Shows how much of your code your tests Coverage
- install `pip3 install coverage`
- run `coverage run --source=todo manage.py test` to run tests in todo
- run `coverage report` to show coverage of code

To find out where you are not covered
- run `coverage html` this creates a dir called htmlcov
- In this is an interactive webpage, so start a http server to view
- run `python3 -m http.server' and navigate to htmlcov/index.html
- Find uncovered code and write tests for them.

## Deploying to heroku with PostgreSQL

- PostgreSQL
- install `pip3 install psycopg2-binary`
- this is so django can use Postgres DB rather than the built in db.sqlite3 file used locally

- Gunicorn
- Web Server the app will run on
- `pip3 install gunicorn`

- Remember to updat requirements.txt
- with `pip3 freeze --local > requirements.txt`

- CLI command for creating a heroku app
- `heroku apps:create django-todo-kelvinhere --region eu`

### Setup a Postgres database
- On the heroku website in your app > resources > find > heroku postgres (select this)
- This adds the postgres resource to the app
- In settings there will now be a DATABASE_URL k,v pair we can access through the apps enviromental variables when deployed on heroku
- You can check the app has this addon by cli `heroku addons`

* If you wanted to use MySQL, the addon above would be called ClearDB instead of 'Heroku Postgres'

#### Setup django to connect to remote database
- `pip3 install dj_database_url`
- This package will allow us to parse the database url that Heroku created.  And get all the connection information out of it.
- Will need to freeze requirements again as this is a new package
- Grab database url from the app on heroku or CLI `heroku config`

* setting.py has database settings make the database have this information
* `import dj_database_url` in this file
* DATABASES = {'default': dj_database_url.parse('your database url from heroku')}

#### PostgresDB production and MySqlite for development
Allow the app to use local db when developing and auto use PostgresDB when 
deployed.

- Check the DIFF for the commit called "DB: Set up a local and deployed database at the same time"

### Deploying

- you may need to update the config below
- `$ heroku config:set DISABLE_COLLECTSTATIC=1`

* Create a procfile to define project as web app with web server
* `web: gunicorn django_todo.wsgi:application` in the procfile tells heroku to launch the app through gunicorn

- When opening the app you will get an error
- 'DisallowedHost at /  Invalid HTTP_HOST header'
- You need to add the url given to solve this to settings.py > ALLOWED_HOSTS as a string

- push to heroku app should be deployed.

### Connect heroku to github
Have heroku auto update to the most current version pushed to github
by linking heroku to the github repo

- Heroku website > your app > deploy > deployment method > github
- Authorise heroku
- Select Enable automatic deploys on the master branch

