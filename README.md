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



## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
