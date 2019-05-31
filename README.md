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

* Go to monolit project folder:
    ```
    $ cd monolit
    ```

* Create .env:
    ```
    $ touch .env
    ```
    with content:
    ```
    DEBUG=True
    ALLOWED_HOSTS=monolit.site|www.monolit.site
    SECRET_KEY=1mnn8bj$(zm5$t9=io*_1ndo43w2p5kv$+sn(xf%d@2so7v_&#
    ```
* Install node packages
    ```
    $ cd monolit\monolit
    $ npm i
    ```

* Compile with Webpack:
    ```
    $ nmp run build
    ```

* Run migrations:
    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

* Create Superuser:
    ```
    $ python manage.py createsuperuser
    then create superuser account
    ```

* Create default content:
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
