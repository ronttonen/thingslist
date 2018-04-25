The main page will display all the Things, sorted by last edit time
A page to create a Thing
A page to edit a Thing (+ button to remove)
A page to view an announce
A page to contact the author of an announce
There are no user accounts; anyone can create an announce anonymously
After the creation, an email should be sent to the user, with a link containing the URL to edit a Thing. The URL must contain a unique and random token: this will protect the announce to be edited by someone else If a user wants to contact the creator, he or she must fill a form with their email and message. An email will be sent to the creator with the information from the form
Quality
Provide build and installation instructions
Use virtualenv
Use Django version 1.10
To send emails, use Django Console Backend. This will simply print the content of the email in the console
Use SQLite
Using the Generic Django Class-Based View is recommended, but this is not a requirement
You can use Bootstrap or Materialize.css or anything to make it look at least presentable
Tests are not necessary, but are a pre

Start:
python3 -m venv virtenv
 . virtenv/bin/activate
pip install --upgrade pip
pip install django~=1.10
django-admin startproject cragislistforthings
python manage.py startapp things

DBMigrations:
python manage.py makemigrations
python manage.py migrate

Install To Project:
To this app to a project:
In urls.py add url(r'^things/', include('things.urls'))
In settings.py add 'things' in INSTALLED_APPS

Deployment (pythonanywhere):
in Bash:
git clone https://github.com/ronttonen/thingslist.git
mkvirtualenv --python=/usr/bin/python3.4 thingslist-virtualenv
pip install django~=1.10

add path to virtualenv:
/home/ronttonenthings/.virtualenvs/thingslist-virtualenv
edit wsgi file:

import os
import sys

path = '/home/ronttonenthings/thingslist'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'cragislistforthings.settings'
setting.py DEBUG = false
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

add domain to ALLOWED_HOSTS in settings.py ronttonenthings.pythonanywhere.com

host static files from backblaze
replace static file urls with backblaze links

