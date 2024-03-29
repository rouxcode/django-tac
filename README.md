# django-tac

Simple terms and condition notify app  


## Install  
```shell
$ pip install -e git+https://github.com/rouxcode/django-tac@master#egg=django-tac  
```  

## Usage  

### basics
add tac to your installed apps:  
```python
INSTALLED_APPS = (
    'tac',
    '...'
)
```  

add the middleware:  
```python
MIDDLEWARE = [
    '...',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'tac.middleware.TACMiddleware',
    '...'
]

if desired load initial data  
```shell
$ ./manage.py tac_load_inital
```
or create at least one popupcontent entry  

use the template tag:
```html
{% load tac_tags %}
{% tac_popup %}
```
or if rouxcode/django-text-ckeditor is not installed
```html
{% tac_popup_no_ckeditor %}
```

### javascript  
jquery needs to be loaded before:  
```html
{% load static %}
<script src="{% static 'tac/tac.js' %}"></script>
```
project urls.py  
```python
urlpatterns = [
    path(
        'tac/',
        include('tac.urls')
    )
    '...'
]
```
