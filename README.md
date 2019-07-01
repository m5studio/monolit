# Monolit README

## How to deploy
### 1. Create virtualenv:
```
$ virtualenv venv
```

**Activate venv:**  

*for Windows*
```
$ venv\Scripts\activate
```

*for Linux*
```
$ source venv\bin\activate
```


### 2. Install packages from requirements.txt:
```
$ pip install -r monolit\requirements\requirements.txt
```


### 3. If you need to update all Python packages
List outdated packages
```
$ pip list --outdated
```

Update all outdated packages Manually
```
$ pip install django, pip, pillow --update
```

Update all outdated packages
```
$ pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -
```


### 4. Go to monolit project folder:
```
$ cd monolit/
```


### 5. Create .env:
```
$ touch .env
```

with content:
```
DEBUG=True
ALLOWED_HOSTS=monolit.site|www.monolit.site
SECRET_KEY=1mnn8bj$(zm5$t9=io*_1ndo43w2p5kv$+sn(xf%d@2so7v_&#
```


### 6. Install & Update node packages
**Install node packages**
```
$ cd monolit\monolit
$ npm i
```

**Update node packages**
```
$ npm update --save-dev
$ npm update --save
```


### 7. Compile with Webpack:
```
$ npm run build
```


### 8. Run migrations:
```
$ python manage.py makemigrations
$ python manage.py migrate
```


### 9. Create Superuser:
```
$ python manage.py createsuperuser
```
then answer the questions in order to create Superuser account


### 10. Create default content:
```
$ python manage.py add_default_content
```


### 11. Run local server:
```
$ python manage.py runserver
```



## How to get from GitHub
Clone from GitHub:
```
$ git clone https://github.com/m5studio/monolit.git
then enter credentials
```


## How to update from GitHub
Run:
```
$ cd monolit\monolit
$ git pull
then enter credentials
```

## Clean empty folders and unused files
Run:
```
$ python manage.py cleanup_unused_media
$ python manage.py clean_empty_media_dirs
```
