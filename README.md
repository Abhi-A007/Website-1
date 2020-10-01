# GreenClothaWay : An Amazing Project

## Prerequisites
`python >= 3.6`

`pip3 lts`

`python-virtualenv`

## Preperation
Create a virtual environment and update PIP and wheel
```
python3 -m venv <venvname>
source <venvname>/bin/activate
pip install -U pip
pip install -U wheel
```

## Installation
Install package. One can find the releases [here](https://github.com/GreenClothaWay/Blog/tree/master/release) 
```
pip install greenclothaway-<release_version>-py3-none-any.whl
```

## Configuration
```
mv <venvname>/lib/python3.8/site-packages/website/settings.py.sample <venvname>/lib/python3.8/site-packages/website/settings.py
```

Now in this settings.py , You have to add a Django Secret Key.
You can also create a Secret Key by this python oneliner : 

```python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'```

For a development server any random 50 character long string will do.
Also , If you want to use another database then the default(sqlite) , You have to configure it here.

After that you will have to create a SuperUser and migrate Django database stuff'n all.

```
manage.py makemigrations
manage.py migrate
manage.py createsuperuser
```
The manage.py command will be available in your virtual environment after the installation.

Now you're all set to turn on your testserver on localhost!!

```
manage.py runserver
```


If you want to run this application on a productive server ,  You'll have to set up a webserver and configure it according to Djangos how to;

But thats on you dude!!
