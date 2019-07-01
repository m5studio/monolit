# Monolit README

## How to deploy
1. Create virtualenv:
    ```
    virtualenv venv
    ```
    activate venv:    
    * for win
        ```
        $ venv\Scripts\activate
        ```

    * for linux
        ```
        $ source venv\bin\activate
        ```

2. Go to monolit project folder:
    ```
    $ cd monolit
    ```

3. Create .env:
    ```
    $ touch .env
    ```
    with content:
    ```
    DEBUG=True
    ALLOWED_HOSTS=monolit.site|www.monolit.site
    SECRET_KEY=1mnn8bj$(zm5$t9=io*_1ndo43w2p5kv$+sn(xf%d@2so7v_&#
    ```
4. Install node packages
    ```
    $ cd monolit\monolit
    $ npm i
    ```

5. Compile with Webpack:
    ```
    $ nmp run build
    ```

6. Run migrations:
    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

7. Create Superuser:
    ```
    $ python manage.py createsuperuser
    then create superuser account
    ```

8. Create default content:
    ```
    $ python manage.py add_default_content
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
