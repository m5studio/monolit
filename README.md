# Monolit README

## How to deploy
1. Create virtualenv:
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
1. Install packages from requirements.txt:
    ```
    $ pip install -r monolit\requirements\requirements.txt
    ```

1. If you need to update all Python packages

    **List outdated packages**
    ```
    $ pip list --outdated
    $ pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -
    ```

    **Update all outdated packages Manually**
    ```
    $ pip install django, pip, pillow --update
    $ pip install django, pip, pillow --upgrade
    ```

    **Update all outdated packages**
    ```
    $ pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -
    ```

1. Go to monolit project folder:
    ```
    $ cd monolit/
    ```

1. Create .env:
    ```
    $ touch .env
    ```

    with content:
    ```
    DEBUG=True
    ALLOWED_HOSTS=monolit.site|www.monolit.site
    SECRET_KEY=1mnn8bj$(zm5$t9=io*_1ndo43w2p5kv$+sn(xf%d@2so7v_&#
    ```
1. Install & Update node packages  

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

1. Compile with Webpack:
    ```
    $ npm run build
    ```

1. Run migrations:
    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

1. Create Superuser:
    ```
    $ python manage.py createsuperuser
    ```
    then answer the questions in order to create Superuser account

1. Create default content:
    ```
    $ python manage.py add_default_content
    ```

1. Run local server:
    ```
    $ python manage.py runserver
    ```


## How to get from GitHub
1. Clone from GitHub:
    ```
    $ git clone https://github.com/m5studio/monolit.git
    then enter credentials
    ```


## How to update from GitHub
1. Run:
    ```
    $ cd monolit\monolit
    $ git pull
    then enter credentials
    ```

## Clean empty folders and unused files
    Run
    ```
    $ python manage.py cleanup_unused_media
    $ python manage.py clean_empty_media_dirs
    ```
