# what-to-eat-backend
Backend for a ML-based restaurant recommendation app

## Setup
1. Install Python 3.6+, run `pip install pipenv`

2. If using VS Code, recommend installing Python extension and make sure select the correct Python3 for the extension.

Add this part for your configurations in settings.json

```JSON
    // This part is for debugging single python file
    {
        "type": "python",
        "request": "launch",
        "name": "Debug Python",
        "program": "${file}",
        "console": "internalConsole"
    },
    // This part is for debugging django server
    {
        "name": "Python : Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/src/manage.py",
        "args": ["runserver", "--noreload"],
        "django": true
    }
```

and add this to settings.json as well

```JSON
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.pycodestyleEnabled": true,
    "python.linting.pycodestyleArgs": [
        "--ignore=E501"
    ],
    "python.pythonPath": "venv/bin/python",
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.inheritEnv": true,
    // Google the following if you are not using MacOS
    "terminal.integrated.env.osx": {
        "PYTHONPATH": "${workspaceFolder}",
    },
```

3. If you don't know the syntax of Python yet, https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7 is a good start

4. A good resource for writing beautiful Python Code: https://realpython.com/python-pep8/

5. Familiar yourself with the following flow of writing code and create pull requests (you can also do these through UI through cmd+T then type "git" in VS Code):

```Bash
# Example workflow for contributing to a project:
$ git clone https://github.com/greatday4april/what-to-eat-backend.git
$ cd what-to-eat-backend

# creates and enable virtual environment
$ pipenv shell

# ( after making some changes ... )
$ git add . && git commit -m "bug fixes"

# pull the latest changes from remote master
$ git pull

# push the changes to master
$ git push
```

6. run `pipenv install` in root folder to install all packages required by the respective stack

7. everytime to install a new package, use `pipenv install whatever-package-name`

8. whenever coding, make sure you are in virtual environment first

9. Google and StackOverflow are your best friends

Good luck coding! and ... lots of debugging probably.
