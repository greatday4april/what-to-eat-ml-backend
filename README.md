# what-to-eat-backend

Backend for a ML-based restaurant recommendation app

![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=greatday4april&show_icons=true&theme=radical&count_private=true)


## [Development Setup Instructions](https://github.com/greatday4april/what-to-eat-ml-backend/wiki/Development-Setup)

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

## Routes

### API Endpoint

Postman Collection: https://www.getpostman.com/collections/4712922ca4a21fcdb2aa

#### Session

* GET `/api/session/` - create or get session, take `user_id` and `page_size`

#### Preference
* GET `/api/preferences/` - create a user preference, take `user_id`
* POST `/api/preferences/` - return favorites list, take `user_id`, `type`, `restaurant_id`

#### User
* GET `/api/user/` - return a user, take `user_id`
* POST `/api/user/` - create a user, take `password`, `cuisine_tags`

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

## Content-based Recommendation

1. make sure Python extension is installed in VS Code and you have done `pipenv install`
2. open the `.ipynb` file in VS Code, and choose to trust the file
3. execute each chunk of code in the notebook, observe the results
4. tweak the parameters/output/input in python code and check your own interesting results
