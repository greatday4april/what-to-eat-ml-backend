# what-to-eat-backend

Backend for a ML-based restaurant recommendation app

## Setup

1. Install Python 3.6+ and PostgreSQL, run `pip install pipenv`

2. in your terminal, run `psql` and then `CREATE DATABASE what_to_eat;`

3. For starters,

```Bash
# Example workflow for contributing to a project:
$ git clone https://github.com/greatday4april/what-to-eat-ml-backend.git
$ cd what-to-eat-ml-backend

# install all required packages
$ pipenv install

# creates and enable virtual environment
$ pipenv shell

# setup the database
$ python manage.py migrate
```

3. Install Python extension for VS Code, and then select the intepreter as the one with `pipenv` ( command+shift+p "Python: Select Intepreter)

4. Add this part for your configurations in settings.json

```JSON
    // This is for running single python file
    {
        "type": "python",
        "request": "launch",
        "name": "Python",
        "program": "${file}",
        "console": "internalConsole",
    },
    // This part is for debugging django server
    {
        "name": "Python : Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/manage.py",
        "args": ["runserver"],
        "django": true,
        "console": "internalConsole"
    },
```

and add this to settings.json as well

```JSON
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.pycodestyleEnabled": true,
    "python.linting.pycodestyleArgs": [
        "--ignore=E501"
    ],
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.inheritEnv": true,
    // Google the following if you are not using MacOS
    "terminal.integrated.env.osx": {
        "DJANGO_SETTINGS_MODULE": "config.settings",
        "PYTHONPATH": "${workspaceFolder}:."
    },
```

5. If you don't know the syntax of Python yet, https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7 is a good start

6. A good resource for writing beautiful Python Code: https://realpython.com/python-pep8/

## run and debug django backend

1. run the "Python : Django" debugger from vscode, or `python3 manage.py runserver`, then visit `http://127.0.0.1:8000`

2. when running "Python : Django" debugger option, you can also use the DEBUG CONSOLE in vscode as your console (similar to rails c)

3. you can also write tests in `tests.py` so you can write some test code for models etc and use "Python" debugger option to run it, or just `python3 tests.py`

## development

1. Familiar yourself with the following flow of writing code and create pull requests (you can also do these through UI through cmd+T then type "git" in VS Code):

```Bash
# ( after making some changes ... )
$ git add . && git commit -m "bug fixes"

# pull the latest changes from remote master
$ git pull

# push the changes to master
$ git push
```

2. whenever coding, make sure you are in virtual environment first: you can either do `pipenv shell` or you can just open any python file and then open a new terminal in vscode, it will automatically activate the virtual environment (because you have done step #3 in setup)

3. everytime to install a new package, use `pipenv install whatever-package-name`

4. Google and StackOverflow are your best friends

Good luck coding! and ... lots of debugging probably.

## Postgres Database Schema

### `preference`

| column name     |  data type   | details |
| --------------- | :----------: | ------: |
| `id`            |    Number    |         |
| `restaurant_id` |     Text     |         |
| `type`          |     Text     |         |
| `created_at`    |  Date/time   |         |
| `user`          | Reference_id |         |

### `user`

| column name     | data type | details |
| --------------- | :-------: | ------: |
| `id`            |  Number   |         |
| `last_login`    | Date/time |         |
| `session_token` |   Text    |         |
| `date_joined`   | Date/time |         |



## Content-based Recommender 

1. download the csv and jupyter notebook, recommended in the same folder 
2. make sure jupyter notebook is installed
3. type "jupyter notebook" in console and hit enter
4. execute each chunk of code in the notebook, observe the results
5. tweak the parameters/output/input in python code
6. check your own interetsing results


