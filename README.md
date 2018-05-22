# django-tac

Simple terms and condition notify app  


## Install  
```shell
$ pip install -e git+https://github.com/rouxcode/django-tac@0.0.3#egg=django-tac  
```  

## Usage  
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
    'tac.middleware.TACMiddleware',
    '...'
]
````

if desired load initial data  
```shell
$ ./manage.py tac_load_inital
```
or create at least one popupcontent entry  

use the template tag:
```html
{% tac_popup %}
```

if desired js (jquery needs to be loaded before):  
```html
<script src="{{ STATIC_URL }}tac/js/tac.accept.js"></script>
```
