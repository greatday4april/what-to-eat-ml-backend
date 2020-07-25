# what-to-eat-backend

Backend for a ML-based restaurant recommendation app

## Setup

1. Install Python 3.6+, run `pip install pipenv`

2. For starters,

```Bash
# Example workflow for contributing to a project:
$ git clone https://github.com/greatday4april/what-to-eat-ml-backend.git
$ cd what-to-eat-ml-backend

# install all required packages
$ pipenv install

# creates and enable virtual environment
$ pipenv shell
```

3. Install Python extension for VS Code, and then select the intepreter as the one with `pipenv` ( command+shift+p "Python: Select Intepreter)

4. Add this part for your configurations in settings.json

```JSON
    // This part is for debugging django server
      {
        "name": "Python : Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/manage.py",
        "args": ["runserver", "--noreload"],
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
        "DJANGO_SETTINGS_MODULE": "what_to_eat.settings",
        "PYTHONPATH": "${workspaceFolder}"
    },
```

5. If you don't know the syntax of Python yet, https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7 is a good start

6. A good resource for writing beautiful Python Code: https://realpython.com/python-pep8/

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
