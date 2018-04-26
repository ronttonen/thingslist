###### Instructions
*The main page will display all the Things, sorted by last edit time <br />
A page to create a Thing <br />
A page to edit a Thing (+ button to remove) <br />
A page to view an announce <br />
A page to contact the author of an announce <br />
There are no user accounts; anyone can create an announce anonymously <br />
After the creation, an email should be sent to the user, with a link containing the URL to edit a Thing. <br />
The URL must contain a unique and random token: this will protect the announce to be edited by someone else If a user wants to contact the creator, he or she must fill a form with their email and message. <br />
An email will be sent to the creator with the information from the form
Quality <br />
Provide build and installation instructions <br />
Use virtualenv <br />
Use Django version 1.10 <br />
To send emails, use Django Console Backend. This will simply print the content of the email in the console <br />
Use SQLite <br />
Using the Generic Django Class-Based View is recommended, but this is not a requirement <br />
You can use Bootstrap or Materialize.css or anything to make it look at least presentable <br />
Tests are not necessary, but are a pre<br />* 

###### Create Django App: <br />
sudo apt install python3-venv <br />
python3 -m venv virtenv <br />
 . virtenv/bin/activate <br />
pip install --upgrade pip <br />
pip install django~=1.10 <br />
django-admin startproject craigslistforthings <br />
cd craigslistforthings <br />
python manage.py startapp things <br />

###### DBMigrations: <br />
python manage.py makemigrations <br />
python manage.py migrate <br />

###### Install To Project: <br />
To add this app to a project: <br />
In urls.py add url(r'^things/', include('things.urls')) <br />
In settings.py add 'things' in INSTALLED_APPS <br />

###### Deployment (pythonanywhere): <br />
in Bash: <br />
git clone https://github.com/ronttonen/thingslist.git <br />
mkvirtualenv --python=/usr/bin/python3.4 thingslist-virtualenv <br />
pip install django~=1.10 <br />

add path to virtualenv: <br />
/home/ronttonenthings/.virtualenvs/thingslist-virtualenv <br />
edit wsgi file: <br />

import os <br />
import sys <br />

path = '/home/ronttonenthings/thingslist' <br />
if path not in sys.path: <br />
    sys.path.append(path) <br />

os.environ['DJANGO_SETTINGS_MODULE'] = 'craigslistforthings.settings' <br />
setting.py DEBUG = false <br />
from django.core.wsgi import get_wsgi_application <br />
application = get_wsgi_application() <br />

add domain to ALLOWED_HOSTS in settings.py ronttonenthings.pythonanywhere.com <br />

host static files from backblaze <br />
replace static file urls with backblaze links <br />

