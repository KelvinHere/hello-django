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


